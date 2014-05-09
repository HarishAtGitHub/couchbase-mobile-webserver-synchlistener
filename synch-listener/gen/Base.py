import re
import json
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('conf/settings.conf')
server_url = config.get('webserver', 'serverUrl')
token_key = config.get('couchbase', 'key')

class AutoVivification(dict):
    def __missing__(self, missingkey):
        self[missingkey] = type(self)()
        return self[missingkey]

class BaseObjects:
    pass

class BaseCRUDObjects(BaseObjects):
    def get(self, document):
        import requests

        pass

    def post(self, document):
        import requests
        jsondoc = self.postParams(document)
        response = requests.post("%s?token=%s" %(server_url + self.url, token_key), data=json.dumps(jsondoc))
        return response

    def put(self, document):
        import requests
        jsondoc = self.putParams(document)
        response = requests.put("%s?token=%s" %(server_url + self.url, token_key), data=json.dumps(jsondoc))
        return response


    def delete(self, document):
        import requests
        self.deleteParams(document)
        response = requests.delete("%s?token=%s" %(server_url + self.url, token_key))
        return response

    def getlist(self, document):
        import requests

        pass


