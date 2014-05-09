import re
from Base import BaseCRUDObjects,AutoVivification

class Appliancemakes(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/appliancemakes'
        return

    def postParams(self, document):
        url = '/api/v1/appliancemakes'
        appliancemake = AutoVivification()
        appliancemake['description'] = document['descriptionText']
        appliancemake['uuid'] = document['uuid']
        appliancemake['order'] = document['order']
        appliancemake = {'appliancemake' :appliancemake}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return appliancemake

    def getParams(self, document):
        url = '/api/v1/appliancemakes/{applianceMakeId}'
        return

    def putParams(self, document):
        url = '/api/v1/appliancemakes/{id}'
        appliancemake = AutoVivification()
        id = document['id']
        appliancemake['description'] = document['descriptionText']
        appliancemake['order'] = document['order']
        appliancemake = {'appliancemake' :appliancemake}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return appliancemake

    def deleteParams(self, document):
        url = '/api/v1/appliancemakes/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

