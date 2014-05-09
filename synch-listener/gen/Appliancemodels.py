import re
from Base import BaseCRUDObjects,AutoVivification

class Appliancemodels(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/appliancemakes/{applianceMakeId}/appliancemodels'
        return

    def postParams(self, document):
        url = '/api/v1/appliancemakes/{applianceMakeId}/appliancemodels'
        appliancemodel = AutoVivification()
        applianceMakeId = document['applianceMakeId']
        appliancemodel['description'] = document['descriptionText']
        appliancemodel['settingsAppliancetypesid'] = document['settingsAppliancetypesid']
        appliancemodel['order'] = document['order']
        appliancemodel['uuid'] = document['uuid']
        appliancemodel = {'appliancemodel' :appliancemodel}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return appliancemodel

    def getParams(self, document):
        url = '/api/v1/appliancemakes/{applianceMakeId}/appliancemodels/{applianceModelId}'
        return

    def putParams(self, document):
        url = '/api/v1/appliancemakes/{applianceMakeId}/appliancemodels/{id}'
        appliancemodel = AutoVivification()
        applianceMakeId = document['applianceMakeId']
        id = document['id']
        appliancemodel['description'] = document['descriptionText']
        appliancemodel['settingsAppliancetypesid'] = document['settingsAppliancetypesid']
        appliancemodel['order'] = document['order']
        appliancemodel = {'appliancemodel' :appliancemodel}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return appliancemodel

    def deleteParams(self, document):
        url = '/api/v1/appliancemakes/{applianceMakeId}/appliancemodels/{id}'
        applianceMakeId = document['applianceMakeId']
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

