import re
from Base import BaseCRUDObjects,AutoVivification

class Telephonetype(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/telephonetypes'
        return

    def postParams(self, document):
        url = '/api/v1/telephonetypes'
        telephonetype = AutoVivification()
        telephonetype['description'] = document['descriptionText']
        telephonetype['uuid'] = document['uuid']
        telephonetype = {'telephonetype' :telephonetype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return telephonetype

    def getParams(self, document):
        url = '/api/v1/telephonetypes/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/telephonetypes/{id}'
        telephonetype = AutoVivification()
        id = document['id']
        telephonetype['description'] = document['descriptionText']
        telephonetype = {'telephonetype' :telephonetype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return telephonetype

    def deleteParams(self, document):
        url = '/api/v1/telephonetypes/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

