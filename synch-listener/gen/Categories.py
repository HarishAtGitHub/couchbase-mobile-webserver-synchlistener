import re
from Base import BaseCRUDObjects,AutoVivification

class Categories(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/categories'
        return

    def postParams(self, document):
        url = '/api/v1/categories'
        category = AutoVivification()
        category['description'] = document['descriptionText']
        category['uuid'] = document['uuid']
        category = {'category' :category}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return category

    def getParams(self, document):
        url = '/api/v1/categories/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/categories/{id}'
        category = AutoVivification()
        id = document['id']
        category['description'] = document['descriptionText']
        category = {'category' :category}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return category

    def deleteParams(self, document):
        url = '/api/v1/categories/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

