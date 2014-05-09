import re
from Base import BaseCRUDObjects,AutoVivification

class Appliancetypes(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/appliancegroups/{applianceGroupId}/appliancetypes'
        return

    def postParams(self, document):
        url = '/api/v1/appliancegroups/{applianceGroupId}/appliancetypes'
        appliancetypes = AutoVivification()
        applianceGroupId = document['applianceGroupId']
        appliancetypes['description'] = document['descriptionText']
        appliancetypes['uuid'] = document['uuid']
        appliancetypes = {'appliancetypes' :appliancetypes}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return appliancetypes

    def getParams(self, document):
        url = '/api/v1/appliancegroups/{applianceGroupId}/appliancetypes/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/appliancegroups/{applianceGroupId}/appliancetypes/{id}'
        appliancetypes = AutoVivification()
        applianceGroupId = document['applianceGroupId']
        id = document['id']
        appliancetypes['description'] = document['descriptionText']
        appliancetypes = {'appliancetypes' :appliancetypes}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return appliancetypes

    def deleteParams(self, document):
        url = '/api/v1/appliancegroups/{applianceGroupId}/appliancetypes/{id}'
        applianceGroupId = document['applianceGroupId']
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

