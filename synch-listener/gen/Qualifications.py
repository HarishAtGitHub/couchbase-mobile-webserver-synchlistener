import re
from Base import BaseCRUDObjects,AutoVivification

class Qualifications(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/qualifications'
        return

    def postParams(self, document):
        url = '/api/v1/qualifications'
        qualification = AutoVivification()
        qualification['description'] = document['descriptionText']
        qualification['uuid'] = document['uuid']
        qualification = {'qualification' :qualification}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return qualification

    def getParams(self, document):
        url = '/api/v1/qualifications/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/qualifications/{id}'
        qualification = AutoVivification()
        id = document['id']
        qualification['description'] = document['descriptionText']
        qualification = {'qualification' :qualification}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return qualification

    def deleteParams(self, document):
        url = '/api/v1/qualifications/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

