import re
from Base import BaseCRUDObjects,AutoVivification

class ServiceReminders(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/servicereminders'
        return

    def postParams(self, document):
        url = '/api/v1/servicereminders'
        servicereminder = AutoVivification()
        servicereminder['name'] = document['name']
        servicereminder['uuid'] = document['uuid']
        servicereminder['order'] = document['order']
        servicereminder = {'servicereminder' :servicereminder}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return servicereminder

    def getParams(self, document):
        url = '/api/v1/servicereminders/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/servicereminders/{id}'
        servicereminder = AutoVivification()
        id = document['id']
        servicereminder['name'] = document['name']
        servicereminder['order'] = document['order']
        servicereminder = {'servicereminder' :servicereminder}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return servicereminder

    def deleteParams(self, document):
        url = '/api/v1/servicereminders/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

