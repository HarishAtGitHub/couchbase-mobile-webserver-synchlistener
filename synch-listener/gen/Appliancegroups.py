import re
from Base import BaseCRUDObjects,AutoVivification

class Appliancegroups(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/appliancegroups'
        return

    def postParams(self, document):
        url = '/api/v1/appliancegroups'
        appliancegroup = AutoVivification()
        appliancegroup['description'] = document['descriptionText']
        appliancegroup['uuid'] = document['uuid']
        appliancegroup['order'] = document['order']
        appliancegroup = {'appliancegroup' :appliancegroup}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return appliancegroup

    def getParams(self, document):
        url = '/api/v1/appliancegroups/{applianceGroupId}'
        return

    def putParams(self, document):
        url = '/api/v1/appliancegroups/{id}'
        appliancegroup = AutoVivification()
        id = document['id']
        appliancegroup['description'] = document['descriptionText']
        appliancegroup['order'] = document['order']
        appliancegroup = {'appliancegroup' :appliancegroup}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return appliancegroup

    def deleteParams(self, document):
        url = '/api/v1/appliancegroups/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

