import re
from Base import BaseCRUDObjects,AutoVivification

class Creditordays(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/creditordays'
        return

    def postParams(self, document):
        url = '/api/v1/creditordays'
        creditorday = AutoVivification()
        creditorday['numberofdays'] = document['numberofdays']
        creditorday['uuid'] = document['uuid']
        creditorday['order'] = document['order']
        creditorday = {'creditorday' :creditorday}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return creditorday

    def getParams(self, document):
        url = '/api/v1/creditordays/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/creditordays/{id}'
        creditorday = AutoVivification()
        id = document['id']
        creditorday['numberofdays'] = document['numberofdays']
        creditorday['order'] = document['order']
        creditorday['default'] = document['default']
        creditorday = {'creditorday' :creditorday}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return creditorday

    def deleteParams(self, document):
        url = '/api/v1/creditordays/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

