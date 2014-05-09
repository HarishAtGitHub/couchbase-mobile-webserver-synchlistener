import re
from Base import BaseCRUDObjects,AutoVivification

class Subcategories(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/categories/{categoriesId}/subcategories'
        return

    def postParams(self, document):
        url = '/api/v1/categories/{categoriesId}/subcategories'
        subcategory = AutoVivification()
        categoriesId = document['categoriesId']
        subcategory['description'] = document['descriptionText']
        subcategory['uuid'] = document['uuid']
        subcategory = {'subcategory' :subcategory}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return subcategory

    def getParams(self, document):
        url = '/api/v1/categories/{categoriesId}/subcategories/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/categories/{categoriesId}/subcategories/{id}'
        subcategory = AutoVivification()
        categoriesId = document['categoriesId']
        id = document['id']
        subcategory['description'] = document['descriptionText']
        subcategory = {'subcategory' :subcategory}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return subcategory

    def deleteParams(self, document):
        url = '/api/v1/categories/{categoriesId}/subcategories/{id}'
        categoriesId = document['categoriesId']
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

