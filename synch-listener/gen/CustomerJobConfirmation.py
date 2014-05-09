import re
from Base import BaseCRUDObjects,AutoVivification

class CustomerJobConfirmation(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/customerjobconfirmations'
        return

    def postParams(self, document):
        url = '/api/v1/customerjobconfirmations'
        customerjobconfirmation = AutoVivification()
        customerjobconfirmation['ical'] = document['ical']
        customerjobconfirmation['messages']['email']['subject'] = document['messages']['email']['subject']
        customerjobconfirmation['messages']['email']['message'] = document['messages']['email']['message']
        customerjobconfirmation['messages']['email']['uuid'] = document['messages']['email']['uuid']
        customerjobconfirmation['messages']['sms']['message'] = document['messages']['sms']['message']
        customerjobconfirmation['messages']['sms']['uuid'] = document['messages']['sms']['uuid']
        customerjobconfirmation['messages']['letter']['message'] = document['messages']['letter']['message']
        customerjobconfirmation['messages']['letter']['uuid'] = document['messages']['letter']['uuid']
        customerjobconfirmation = {'customerjobconfirmation' :customerjobconfirmation}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return customerjobconfirmation

