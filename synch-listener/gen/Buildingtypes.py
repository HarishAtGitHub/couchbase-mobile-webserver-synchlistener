import re
from Base import BaseCRUDObjects,AutoVivification

class Buildingtypes(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/buildingtypes'
        return

    def postParams(self, document):
        url = '/api/v1/buildingtypes'
        buildingtype = AutoVivification()
        buildingtype['description'] = document['descriptionText']
        buildingtype['uuid'] = document['uuid']
        buildingtype['order'] = document['order']
        buildingtype = {'buildingtype' :buildingtype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return buildingtype

    def getParams(self, document):
        url = '/api/v1/buildingtypes/{id}'
        return

