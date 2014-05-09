import requests
import json
import sqlite3
import logging
import logstash_formatter
import os
import sys
#sys.path.append('/media/harish/storage/code/python/apidocparser')
from gen import *
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('conf/settings.conf')

base_url = config.get('couchbase', 'bucketUrl')

"""
    1.create logging file  handler
    2.set the formatter in the above handler to logstashformatter
    3.set the updated handler above, in the logger
"""
log_file_location = 'log/synchlistener.log'
if not os.path.exists(log_file_location):
    os.system('touch ' + log_file_location)
handler = logging.FileHandler(log_file_location)
formatter = logstash_formatter.LogstashFormatter()
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)
headers = {'content-type': 'application/json'}

''' *****   sequence number update section  START *****'''
conn = sqlite3.connect(config.get('db', 'dblocation'))
logger.info("Opened database successfully")
channelName = 'public' # can be configured later as per usecase
lastsequencenumber = 0
cursor = conn.execute("SELECT LASTSEQUENCENUMBER FROM TRACKSEQNUMBER WHERE CHANNELNAME=:channelName",{'channelName':channelName});

for row in cursor:
    global lastsequencenumber
    lastsequencenumber =  row[0]

    logger.info('last sequence number before crash was ' + str(lastsequencenumber))

change_listener = requests.get('%s/_changes?feed=continuous&heartbeat=22924&style=all_docs&since=public:%s' %(base_url,lastsequencenumber) , stream=True)

def updateSequenceNumber():

    logger.info('updating the last sequence number to ' + str(lastsequencenumber + 1))
    global lastsequencenumber
    lastsequencenumber = lastsequencenumber + 1
    conn.execute("INSERT OR REPLACE INTO TRACKSEQNUMBER (CHANNELNAME,LASTSEQUENCENUMBER) \
      VALUES (:channelName,:lastSequenceNumber)", {'channelName':channelName,'lastSequenceNumber':lastsequencenumber});
    conn.commit()

''' *****   sequence number update section  END *****'''

# TODO: iter_lines(1) is inefficient, Check with requests api for a better solution
for line in change_listener.iter_lines(1):
    if line:
        changed_node = json.loads(line)

        rev_id = changed_node['changes'][0]['rev']
        doc_uuid = changed_node['id']

        doc_request = requests.get('%s/%s?rev=%s' %(base_url, doc_uuid, rev_id))
        document = doc_request.json()

        # if this change came from server, return back
        if document.has_key('shouldProcess') and document['shouldProcess'] == True:
            pass
        else:
            continue

        # If this has an Id, then its an update from mobile, send
        # PUT or DELETE call, otherwise make a POST
        if document.has_key('id') and document['id'] != '':
            if document['deleted']:



                try:
                    response = eval(str(document['type']))().delete(document)
                    if (response.status_code == 204 ):
                        logger.info("DELETE: Deleted the document in webserver ")
                        updateSequenceNumber()
                except NameError:

                    logger.info("The document type is Invalid .. so will not be synchronised with the webserver")
                    logger.info("The document is : " +  str(document))
                    #TODO put logic to inform mobile about this failure
                except :

                    logger.info("Error occured while synchronizing document : " +  str(document))
                    #TODO put logic to inform mobile about this failure


            else:

                try:
                    response = eval(str(document['type']))().put(document)
                    if (response.status_code == 204 ):
                        logger.info("PUT: Updated the document in webserver ")
                        updateSequenceNumber()
                except NameError:

                    logger.info("The document type is Invalid .. so will not be synchronised with the webserver")
                    logger.info("The document is : " +  str(document))
                    #TODO put logic to inform mobile about this failure
                except :

                    logger.info("Error occured while synchronizing document : " +  str(document))
                    #TODO put logic to inform mobile about this failure

        else:

            try:
                response = Titles().post(document)
                if (response.status_code == 201 ):
                    logger.info({"call-method" : "POST",
                                 "call-status" : "success",
                                 "call-status-code" : response.status_code
                                 })
                    updateSequenceNumber()
            except NameError:

                logger.info({"call-method" : "POST",
                             "call-status" : "failure",
                             "call-status-code" : response.status_code,
                             "error-msg" : "The document type is Invalid .. so will not be synchronised with the webserver",
                             "error-doc" : str(document) })
                #TODO put logic to inform mobile about this failure
            except :

                logger.info({"call-method" : "POST",
                             "call-status" : "failure",
                             "error-msg" : "Error occured while synchronizing document : ",
                             "error-doc" : str(document) })
                #TODO put logic to inform mobile about this failure




