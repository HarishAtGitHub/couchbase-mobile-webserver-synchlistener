import re
from Base import BaseCRUDObjects,AutoVivification

class Pricingitems(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/pricingitems'
        return

    def postParams(self, document):
        url = '/api/v1/pricingitems'
        pricingitem = AutoVivification()
        pricingitem['description'] = document['descriptionText']
        pricingitem['unitprice'] = document['unitprice']
        pricingitem['taxesid'] = document['taxesid']
        pricingitem['uuid'] = document['uuid']
        pricingitem['order'] = document['order']
        pricingitem = {'pricingitem' :pricingitem}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return pricingitem

    def getParams(self, document):
        url = '/api/v1/pricingitems/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/pricingitems/{id}'
        pricingitem = AutoVivification()
        id = document['id']
        pricingitem['description'] = document['descriptionText']
        pricingitem['unitprice'] = document['unitprice']
        pricingitem['taxesid'] = document['taxesid']
        pricingitem['order'] = document['order']
        pricingitem = {'pricingitem' :pricingitem}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return pricingitem

    def deleteParams(self, document):
        url = '/api/v1/pricingitems/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

