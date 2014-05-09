import re
from Base import BaseCRUDObjects,AutoVivification

class Industries(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/industries'
        return

    def postParams(self, document):
        url = '/api/v1/industries'
        industry = AutoVivification()
        industry['description'] = document['descriptionText']
        industry['uuid'] = document['uuid']
        industry['order'] = document['order']
        industry = {'industry' :industry}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return industry

    def getParams(self, document):
        url = '/api/v1/industries/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/industries/{id}'
        industry = AutoVivification()
        id = document['id']
        industry['description'] = document['descriptionText']
        industry['order'] = document['order']
        industry = {'industry' :industry}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return industry

    def deleteParams(self, document):
        url = '/api/v1/industries/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

