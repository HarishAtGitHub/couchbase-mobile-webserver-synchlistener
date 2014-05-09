import re
from Base import BaseCRUDObjects,AutoVivification

class StockLocation(BaseCRUDObjects):
    def postParams(self, document):
        url = '/api/v1/stocklocations'
        stocklocation = AutoVivification()
        stocklocation['description'] = document['descriptionText']
        stocklocation['uuid'] = document['uuid']
        stocklocation['order'] = document['order']
        stocklocation = {'stocklocation' :stocklocation}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return stocklocation

    def getParams(self, document):
        url = '/api/v1/stocklocations/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/stocklocations/{id}'
        stocklocation = AutoVivification()
        id = document['id']
        stocklocation['description'] = document['descriptionText']
        stocklocation['order'] = document['order']
        stocklocation = {'stocklocation' :stocklocation}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return stocklocation

    def deleteParams(self, document):
        url = '/api/v1/stocklocations/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

