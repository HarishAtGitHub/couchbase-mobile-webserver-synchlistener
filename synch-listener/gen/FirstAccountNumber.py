import re
from Base import BaseCRUDObjects,AutoVivification

class FirstAccountNumber(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/firstaccountnumbers'
        return

    def postParams(self, document):
        url = '/api/v1/firstaccountnumbers'
        firstaccountnumber = AutoVivification()
        firstaccountnumber['value'] = document['value']
        firstaccountnumber['uuid'] = document['uuid']
        firstaccountnumber = {'firstaccountnumber' :firstaccountnumber}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return firstaccountnumber

