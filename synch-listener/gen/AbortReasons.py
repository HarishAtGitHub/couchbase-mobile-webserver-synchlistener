import re
from Base import BaseCRUDObjects,AutoVivification

class AbortReasons(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/abortreasons'
        return

    def postParams(self, document):
        url = '/api/v1/abortreasons'
        abortreason = AutoVivification()
        abortreason['description'] = document['descriptionText']
        abortreason['uuid'] = document['uuid']
        abortreason['order'] = document['order']
        abortreason = {'abortreason' :abortreason}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return abortreason

    def getParams(self, document):
        url = '/api/v1/abortreasons/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/abortreasons/{id}'
        abortreason = AutoVivification()
        id = document['id']
        abortreason['description'] = document['descriptionText']
        abortreason['order'] = document['order']
        abortreason = {'abortreason' :abortreason}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return abortreason

    def deleteParams(self, document):
        url = '/api/v1/abortreasons/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

