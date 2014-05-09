import re
from Base import BaseCRUDObjects,AutoVivification

class Fueltypes(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/fueltypes'
        return

    def postParams(self, document):
        url = '/api/v1/fueltypes'
        fueltype = AutoVivification()
        fueltype['description'] = document['descriptionText']
        fueltype['uuid'] = document['uuid']
        fueltype['order'] = document['order']
        fueltype = {'fueltype' :fueltype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return fueltype

    def getParams(self, document):
        url = '/api/v1/fueltypes/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/fueltypes/{id}'
        fueltype = AutoVivification()
        id = document['id']
        fueltype['description'] = document['descriptionText']
        fueltype['order'] = document['order']
        fueltype = {'fueltype' :fueltype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return fueltype

    def deleteParams(self, document):
        url = '/api/v1/fueltypes/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

