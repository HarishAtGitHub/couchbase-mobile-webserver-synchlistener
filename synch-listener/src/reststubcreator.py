from __future__ import print_function
from bs4 import BeautifulSoup
import re
import os
import shutil
import requests

''' To create python modules where we can place generated file '''
#comment the following to have gen folder in the same folder as rest_stub.py
os.chdir('..')
generated_files_container_name = 'gen'
modules_list = []
def createPythonModule():
    os.mkdir(generated_files_container_name)
    #TODO :using system touch now . replace later with the python equivalent
    os.system('touch ' + os.getcwd() + os.sep + generated_files_container_name + os.sep + '__init__.py')

if not os.path.exists(generated_files_container_name):
    createPythonModule()
else:
    shutil.rmtree(generated_files_container_name)
    createPythonModule()

base_folder = os.getcwd()
baseclass_file = open(base_folder + os.sep + generated_files_container_name + os.sep + 'Base.py', "wb")
os.chdir('..')
print("""import re
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

""", file=baseclass_file)
r  = requests.get("http://www.commusoft4.co.uk/webservice_dev.php/api/doc/")
#soup = BeautifulSoup(open('/media/harish/storage/code/python/regex/APIdoc.html'))
soup = BeautifulSoup(r.text)

for div in soup.find_all("div", { "id" : "section" }):
    t = div.h1.string
    base_class_name = t.replace(" ", "")
    #print('',file=subclass_file )
    subclass_file = open(base_folder +  os.sep + generated_files_container_name + os.sep + base_class_name + '.py', "wb")
    print("""import re
from Base import BaseCRUDObjects,AutoVivification
""", file=subclass_file)
    print('class ' + base_class_name + '(BaseCRUDObjects):' , file=subclass_file)
    modules_list.append(str(base_class_name)) #making it string as beautiful soup only store unicode strings in its datastructure
                                              #http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html
    for form in div.find_all('form'):
        rest_endpoint = (re.search("\/api\/.*",form.get('action'))).group()
        method_name = form.get('method')
        function_name = ''
        array_name = ''
        param_list = []
        i = 0
        title_additional_params = re.findall('\{([A-Za-z0-9]+)\}$', rest_endpoint)
        if title_additional_params or ( method_name.lower() in ('post','put','delete')):
            print('    ' + 'def ' + method_name.lower() + 'Params' + '(self, document):', file=subclass_file)
        else :
            print('    ' + 'def ' + method_name.lower() + 'Params' + '_list' + '(self, document):', file=subclass_file)
        print ('        ' + 'url' + ' = ' + '\'' + rest_endpoint + '\'', file=subclass_file)
        if ((form.get('method') == 'POST' or form.get('method') == 'PUT' or form.get('method') == 'GET' or form.get('method') == 'DELETE')):
            for fieldset in form.find_all("fieldset", { "class" : "parameters" }):
                for input in fieldset.find_all("input", { "class" : "key" }):
                    #print input.get('value')
                    #if '[' in input.get('value'):
                    if '[' in input.get('value'):
                        temp = []
                        temp_param = input.get('value')
                        brackets = re.findall('\[([A-Za-z0-9_]+)\]',input.get('value') )
                        for bracket in brackets:
                            #print bracket\{([A-Za-z0-9]+)\}
                            temp.append(bracket)
                        for a in temp:
                            if not a.isdigit():
                                temp_param = re.sub('\[' + a + '\]' , '[\'' + a + '\']', temp_param)


                        param_list.append(temp_param)
                    else :
                        param_list.append(input.get('value'))

                    if i == 0:
                        title_search = re.search('([A-Za-z0-9]+)\[',input.get('value') , re.IGNORECASE)
                        if title_search :
                            i = 1;
                            array_name = title_search.group(1)
                            function_name = title_search.group(1).title()
            title_additional_params = re.findall('\{([A-Za-z0-9]+)\}',rest_endpoint )
            if title_additional_params:
                for additional_param in title_additional_params :
                    if 'By' in function_name:
                        function_name = function_name + 'And' + additional_param.title() ;
                    else :
                        function_name = function_name + 'By' + additional_param.title() ;
            """
            print('    ' + 'def ' + method_name.lower() + 'Params' + '(self, document):', file=subclass_file)
            """
            #refactor the following
            if (method_name.lower() == "put" or method_name.lower() == "post" ):
                print('    ' + '    ' + array_name + ' = AutoVivification()', file=subclass_file)

            if (method_name.lower() == "put" or method_name.lower() == "post" or method_name.lower() == "delete"):
                for param in param_list:
                    keys = re.search('(\[.*\])',param , re.IGNORECASE)
                    if keys:
                        print('    ' + '    ' + param + ' = document'  + keys.group(1).replace("description", "descriptionText") , file=subclass_file)
                    else :
                        #check if descriptionText replacement is unncessecary
                        print('    ' + '    ' + param + ' = document[\''  + param.replace("description", "descriptionText") + '\']' , file=subclass_file)
            if (method_name.lower() == "put" or method_name.lower() == "post"):
                print('    ' + '    ' + array_name + ' = {\'' + array_name + '\' :' + array_name +'}' , file=subclass_file  )
            if (method_name.lower() == "put" or method_name.lower() == "post" or method_name.lower() == "delete"):
                #change the following to a global function
                print("""
        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path
""", file=subclass_file)
                print('    ' + '    ' + 'return ' + array_name, file=subclass_file)
            else :
                print('    ' + '    ' + 'return', file=subclass_file)
            print('',file=subclass_file )

    base_class_name = t.replace(" ", "") # resetting base class name to give place for next fresh h2
    subclass_file.close()

init_file = open(base_folder + os.sep + generated_files_container_name + os.sep + '__init__.py', "wb")
#print('__all__ = ' + modules_list.__str__(),file=init_file )
for module in modules_list:
    print('from ' + module + ' import ' + '*',file=init_file )
init_file.close()