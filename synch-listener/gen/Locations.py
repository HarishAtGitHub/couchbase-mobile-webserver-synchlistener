import re
from Base import BaseCRUDObjects,AutoVivification

class Locations(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/locations'
        return

    def postParams(self, document):
        url = '/api/v1/locations'
        location = AutoVivification()
        location['description'] = document['descriptionText']
        location['uuid'] = document['uuid']
        location['order'] = document['order']
        location = {'location' :location}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return location

    def getParams(self, document):
        url = '/api/v1/locations/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/locations/{id}'
        location = AutoVivification()
        id = document['id']
        location['description'] = document['descriptionText']
        location['order'] = document['order']
        location = {'location' :location}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return location

    def deleteParams(self, document):
        url = '/api/v1/locations/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

