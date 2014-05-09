import re
from Base import BaseCRUDObjects,AutoVivification

class Firstinvoicenumbers(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/firstinvoicenumbers'
        return

    def postParams(self, document):
        url = '/api/v1/firstinvoicenumbers'
        firstinvoicenumbertype = AutoVivification()
        firstinvoicenumbertype['invoice_number_type'] = document['invoice_number_type']
        firstinvoicenumbertype['value'] = document['value']
        firstinvoicenumbertype['uuid'] = document['uuid']
        firstinvoicenumbertype = {'firstinvoicenumbertype' :firstinvoicenumbertype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return firstinvoicenumbertype

