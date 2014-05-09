import re
from Base import BaseCRUDObjects,AutoVivification

class PaymentMethods(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/paymentmethods'
        return

    def postParams(self, document):
        url = '/api/v1/paymentmethods'
        paymentMethod = AutoVivification()
        paymentMethod['description'] = document['descriptionText']
        paymentMethod['uuid'] = document['uuid']
        paymentMethod['order'] = document['order']
        paymentMethod = {'paymentMethod' :paymentMethod}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return paymentMethod

    def getParams(self, document):
        url = '/api/v1/paymentmethods/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/paymentmethods/{id}'
        paymentMethod = AutoVivification()
        id = document['id']
        paymentMethod['description'] = document['descriptionText']
        paymentMethod['order'] = document['order']
        paymentMethod = {'paymentMethod' :paymentMethod}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return paymentMethod

    def deleteParams(self, document):
        url = '/api/v1/paymentmethods/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

