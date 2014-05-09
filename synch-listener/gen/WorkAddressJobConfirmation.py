import re
from Base import BaseCRUDObjects,AutoVivification

class WorkAddressJobConfirmation(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/workaddressjobconfirmations'
        return

    def postParams(self, document):
        url = '/api/v1/workaddressjobconfirmations'
        workadrressjobconfirmation = AutoVivification()
        workadrressjobconfirmation['ical'] = document['ical']
        workadrressjobconfirmation['messages']['email']['subject'] = document['messages']['email']['subject']
        workadrressjobconfirmation['messages']['email']['message'] = document['messages']['email']['message']
        workadrressjobconfirmation['messages']['email']['uuid'] = document['messages']['email']['uuid']
        workadrressjobconfirmation['messages']['sms']['message'] = document['messages']['sms']['message']
        workadrressjobconfirmation['messages']['sms']['uuid'] = document['messages']['sms']['uuid']
        workadrressjobconfirmation['messages']['letter']['message'] = document['messages']['letter']['message']
        workadrressjobconfirmation['messages']['letter']['uuid'] = document['messages']['letter']['uuid']
        workadrressjobconfirmation = {'workadrressjobconfirmation' :workadrressjobconfirmation}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return workadrressjobconfirmation

