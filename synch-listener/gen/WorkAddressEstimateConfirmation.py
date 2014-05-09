import re
from Base import BaseCRUDObjects,AutoVivification

class WorkAddressEstimateConfirmation(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/workaddressestimateconfirmations'
        return

    def postParams(self, document):
        url = '/api/v1/workaddressestimateconfirmations'
        workadrressestimateconfirmation = AutoVivification()
        workadrressestimateconfirmation['ical'] = document['ical']
        workadrressestimateconfirmation['messages']['email']['subject'] = document['messages']['email']['subject']
        workadrressestimateconfirmation['messages']['email']['message'] = document['messages']['email']['message']
        workadrressestimateconfirmation['messages']['email']['uuid'] = document['messages']['email']['uuid']
        workadrressestimateconfirmation['messages']['sms']['message'] = document['messages']['sms']['message']
        workadrressestimateconfirmation['messages']['sms']['uuid'] = document['messages']['sms']['uuid']
        workadrressestimateconfirmation['messages']['letter']['message'] = document['messages']['letter']['message']
        workadrressestimateconfirmation['messages']['letter']['uuid'] = document['messages']['letter']['uuid']
        workadrressestimateconfirmation = {'workadrressestimateconfirmation' :workadrressestimateconfirmation}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return workadrressestimateconfirmation

