import re
from Base import BaseCRUDObjects,AutoVivification

class MobileSettings(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/users/{id}/mobilesettings'
        return

    def postParams(self, document):
        url = '/api/v1/users/{id}/mobilesettings'
        mobilesetting = AutoVivification()
        id = document['id']
        mobilesetting['values'][0]['value'] = document['values'][0]['value']
        mobilesetting['values'][1]['value'] = document['values'][1]['value']
        mobilesetting = {'mobilesetting' :mobilesetting}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return mobilesetting

