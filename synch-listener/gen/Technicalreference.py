import re
from Base import BaseCRUDObjects,AutoVivification

class Technicalreference(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/technicalreferences'
        return

    def postParams(self, document):
        url = '/api/v1/technicalreferences'
        technicalreference = AutoVivification()
        technicalreference['description'] = document['descriptionText']
        technicalreference['uuid'] = document['uuid']
        technicalreference = {'technicalreference' :technicalreference}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return technicalreference

    def getParams(self, document):
        url = '/api/v1/technicalreferences/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/technicalreferences/{id}'
        technicalreference = AutoVivification()
        id = document['id']
        technicalreference['description'] = document['descriptionText']
        technicalreference = {'technicalreference' :technicalreference}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return technicalreference

    def deleteParams(self, document):
        url = '/api/v1/technicalreferences/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

