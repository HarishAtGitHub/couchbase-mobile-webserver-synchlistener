import re
from Base import BaseCRUDObjects,AutoVivification

class Todos(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/jobdescriptions/{jobDescriptionId}/todos'
        return

    def postParams(self, document):
        url = '/api/v1/jobdescriptions/{jobDescriptionId}/todos'
        todos = AutoVivification()
        jobDescriptionId = document['jobDescriptionId']
        todos['tablename'] = document['tablename']
        todos['settingsTodocategoriesid'] = document['settingsTodocategoriesid']
        todos['description'] = document['descriptionText']
        todos['uuid'] = document['uuid']
        todos = {'todos' :todos}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return todos

    def putParams(self, document):
        url = '/api/v1/jobdescriptions/{jobDescriptionId}/todos/{id}'
        todos = AutoVivification()
        jobDescriptionId = document['jobDescriptionId']
        id = document['id']
        todos['tablename'] = document['tablename']
        todos['settingsTodocategoriesid'] = document['settingsTodocategoriesid']
        todos['description'] = document['descriptionText']
        todos = {'todos' :todos}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return todos

    def deleteParams(self, document):
        url = '/api/v1/jobdescriptions/{jobDescriptionId}/todos/{id}'
        jobDescriptionId = document['jobDescriptionId']
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

    def getParams(self, document):
        url = '/api/v1/jobdescriptions/{jobDescriptionId}/todos/{toDoId}'
        return

