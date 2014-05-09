import re
from Base import BaseCRUDObjects,AutoVivification

class Titles(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/titles'
        return

    def postParams(self, document):
        url = '/api/v1/titles'
        title = AutoVivification()
        title['description'] = document['descriptionText']
        title['uuid'] = document['uuid']
        title['order'] = document['order']
        title = {'title' :title}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return title

    def getParams(self, document):
        url = '/api/v1/titles/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/titles/{id}'
        title = AutoVivification()
        id = document['id']
        title['description'] = document['descriptionText']
        title['order'] = document['order']
        title = {'title' :title}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return title

    def deleteParams(self, document):
        url = '/api/v1/titles/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

