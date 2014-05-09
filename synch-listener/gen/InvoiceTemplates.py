import re
from Base import BaseCRUDObjects,AutoVivification

class InvoiceTemplates(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/invoicetemplates'
        return

    def postParams(self, document):
        url = '/api/v1/invoicetemplates'
        invoicetemplate = AutoVivification()
        invoicetemplate['value'] = document['value']
        invoicetemplate['uuid'] = document['uuid']
        invoicetemplate = {'invoicetemplate' :invoicetemplate}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return invoicetemplate

