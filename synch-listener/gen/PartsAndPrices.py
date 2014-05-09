import re
from Base import BaseCRUDObjects,AutoVivification

class PartsAndPrices(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/partsandprices'
        return

    def postParams(self, document):
        url = '/api/v1/partsandprices'
        partsandprices = AutoVivification()
        partsandprices['description'] = document['descriptionText']
        partsandprices['settingsIndustryid'] = document['settingsIndustryid']
        partsandprices['settingsSubcategoryid'] = document['settingsSubcategoryid']
        partsandprices['type'] = document['type']
        partsandprices['make'] = document['make']
        partsandprices['model'] = document['model']
        partsandprices['manufacturepartnumber'] = document['manufacturepartnumber']
        partsandprices['price'] = document['price']
        partsandprices['markup'] = document['markup']
        partsandprices['vat'] = document['vat']
        partsandprices['uuid'] = document['uuid']
        partsandprices = {'partsandprices' :partsandprices}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return partsandprices

    def putParams(self, document):
        url = '/api/v1/partsandprices/{id}'
        partsandprices = AutoVivification()
        id = document['id']
        partsandprices['description'] = document['descriptionText']
        partsandprices['settingsIndustryid'] = document['settingsIndustryid']
        partsandprices['settingsSubcategoryid'] = document['settingsSubcategoryid']
        partsandprices['type'] = document['type']
        partsandprices['make'] = document['make']
        partsandprices['model'] = document['model']
        partsandprices['manufacturepartnumber'] = document['manufacturepartnumber']
        partsandprices['price'] = document['price']
        partsandprices['markup'] = document['markup']
        partsandprices['vat'] = document['vat']
        partsandprices = {'partsandprices' :partsandprices}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return partsandprices

    def deleteParams(self, document):
        url = '/api/v1/partsandprices/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

    def getParams(self, document):
        url = '/api/v1/partsandprices/{partsAndPriceId}'
        return

