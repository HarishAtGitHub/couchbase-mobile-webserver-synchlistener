import re
from Base import BaseCRUDObjects,AutoVivification

class NewVehicles(BaseCRUDObjects):
    def postParams(self, document):
        url = '/api/v1/newvehicles'
        newvehicles = AutoVivification()
        newvehicles['registrationnumber'] = document['registrationnumber']
        newvehicles['yearofregistration'] = document['yearofregistration']
        newvehicles['make'] = document['make']
        newvehicles['model'] = document['model']
        newvehicles['uuid'] = document['uuid']
        newvehicles = {'newvehicles' :newvehicles}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return newvehicles

