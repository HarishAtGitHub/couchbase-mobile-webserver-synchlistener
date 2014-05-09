import re
from Base import BaseCRUDObjects,AutoVivification

class BuildingTypes(BaseCRUDObjects):
    def putParams(self, document):
        url = '/api/v1/buildingtypes/{id}'
        buildingtype = AutoVivification()
        id = document['id']
        buildingtype['description'] = document['descriptionText']
        buildingtype['order'] = document['order']
        buildingtype = {'buildingtype' :buildingtype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return buildingtype

    def deleteParams(self, document):
        url = '/api/v1/buildingtypes/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

