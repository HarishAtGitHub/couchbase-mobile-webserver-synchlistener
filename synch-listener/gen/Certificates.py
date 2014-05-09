import re
from Base import BaseCRUDObjects,AutoVivification

class Certificates(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/customcertificates'
        return

    def postParams(self, document):
        url = '/api/v1/customcertificates'
        customcertificate = AutoVivification()
        customcertificate['name'] = document['name']
        customcertificate['description'] = document['descriptionText']
        customcertificate['uuid'] = document['uuid']
        customcertificate['order'] = document['order']
        customcertificate = {'customcertificate' :customcertificate}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return customcertificate

    def getParams(self, document):
        url = '/api/v1/customcertificates/{customCertificateId}'
        return

    def putParams(self, document):
        url = '/api/v1/customcertificates/{id}'
        customcertificate = AutoVivification()
        id = document['id']
        customcertificate['name'] = document['name']
        customcertificate['description'] = document['descriptionText']
        customcertificate['order'] = document['order']
        customcertificate = {'customcertificate' :customcertificate}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return customcertificate

    def deleteParams(self, document):
        url = '/api/v1/customcertificates/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

