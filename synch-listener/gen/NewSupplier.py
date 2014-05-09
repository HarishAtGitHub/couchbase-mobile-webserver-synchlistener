import re
from Base import BaseCRUDObjects,AutoVivification

class NewSupplier(BaseCRUDObjects):
    def postParams(self, document):
        url = '/api/v1/suppliers'
        suppliertype = AutoVivification()
        suppliertype['contacts']['companyname'] = document['contacts']['companyname']
        suppliertype['addressline1'] = document['addressline1']
        suppliertype['addressline2'] = document['addressline2']
        suppliertype['addressline3'] = document['addressline3']
        suppliertype['town'] = document['town']
        suppliertype['county'] = document['county']
        suppliertype['contacts']['contactstelephone'][0]['telephonenumber'] = document['contacts']['contactstelephone'][0]['telephonenumber']
        suppliertype['contacts']['contactsemail']['emailaddress'] = document['contacts']['contactsemail']['emailaddress']
        suppliertype['vatreg'] = document['vatreg']
        suppliertype['creditterms'] = document['creditterms']
        suppliertype['uuid'] = document['uuid']
        suppliertype = {'suppliertype' :suppliertype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return suppliertype

