import re
from Base import BaseCRUDObjects,AutoVivification

class AdvertisingType(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/advertisingtypes'
        return

    def postParams(self, document):
        url = '/api/v1/advertisingtypes'
        advertisingtype = AutoVivification()
        advertisingtype['description'] = document['descriptionText']
        advertisingtype['uuid'] = document['uuid']
        advertisingtype['order'] = document['order']
        advertisingtype = {'advertisingtype' :advertisingtype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return advertisingtype

    def getParams(self, document):
        url = '/api/v1/advertisingtypes/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/advertisingtypes/{id}'
        advertisingtype = AutoVivification()
        id = document['id']
        advertisingtype['description'] = document['descriptionText']
        advertisingtype['order'] = document['order']
        advertisingtype = {'advertisingtype' :advertisingtype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return advertisingtype

    def deleteParams(self, document):
        url = '/api/v1/advertisingtypes/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

