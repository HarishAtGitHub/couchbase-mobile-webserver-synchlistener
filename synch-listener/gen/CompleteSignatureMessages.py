import re
from Base import BaseCRUDObjects,AutoVivification

class CompleteSignatureMessages(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/completesignaturemessages'
        return

    def postParams(self, document):
        url = '/api/v1/completesignaturemessages'
        completesignaturemessage = AutoVivification()
        completesignaturemessage['value'] = document['value']
        completesignaturemessage['uuid'] = document['uuid']
        completesignaturemessage['setup'] = document['setup']
        completesignaturemessage = {'completesignaturemessage' :completesignaturemessage}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return completesignaturemessage

