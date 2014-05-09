import re
from Base import BaseCRUDObjects,AutoVivification

class Branch(BaseCRUDObjects):
    def postParams(self, document):
        url = '/api/v1/customers/{id}/branches'
        branch = AutoVivification()
        id = document['id']
        branch['branchname'] = document['branchname']
        branch['addressline1'] = document['addressline1']
        branch['addressline2'] = document['addressline2']
        branch['addressline3'] = document['addressline3']
        branch['town'] = document['town']
        branch['country'] = document['country']
        branch['postcode'] = document['postcode']
        branch = {'branch' :branch}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return branch

