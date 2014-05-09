import re
from Base import BaseCRUDObjects,AutoVivification

class InvoiceTermsandConditions(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/invoicetermsandconditions'
        return

    def postParams(self, document):
        url = '/api/v1/invoicetermsandconditions'
        invoicetermsandconditions = AutoVivification()
        invoicetermsandconditions['message'] = document['message']
        invoicetermsandconditions = {'invoicetermsandconditions' :invoicetermsandconditions}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return invoicetermsandconditions

