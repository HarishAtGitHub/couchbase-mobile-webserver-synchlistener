import re
from Base import BaseCRUDObjects,AutoVivification

class FreeOfChargeReasons(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/freeofchargereasons'
        return

    def postParams(self, document):
        url = '/api/v1/freeofchargereasons'
        freeofchargereason = AutoVivification()
        freeofchargereason['description'] = document['descriptionText']
        freeofchargereason['uuid'] = document['uuid']
        freeofchargereason = {'freeofchargereason' :freeofchargereason}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return freeofchargereason

    def getParams(self, document):
        url = '/api/v1/freeofchargereasons/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/freeofchargereasons/{id}'
        freeofchargereason = AutoVivification()
        id = document['id']
        freeofchargereason['description'] = document['descriptionText']
        freeofchargereason = {'freeofchargereason' :freeofchargereason}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return freeofchargereason

    def deleteParams(self, document):
        url = '/api/v1/freeofchargereasons/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

