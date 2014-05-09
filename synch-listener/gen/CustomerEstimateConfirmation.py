import re
from Base import BaseCRUDObjects,AutoVivification

class CustomerEstimateConfirmation(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/customerestimateconfirmations'
        return

    def postParams(self, document):
        url = '/api/v1/customerestimateconfirmations'
        customerestimateconfirmation = AutoVivification()
        customerestimateconfirmation['ical'] = document['ical']
        customerestimateconfirmation['messages']['email']['subject'] = document['messages']['email']['subject']
        customerestimateconfirmation['messages']['email']['message'] = document['messages']['email']['message']
        customerestimateconfirmation['messages']['email']['uuid'] = document['messages']['email']['uuid']
        customerestimateconfirmation['messages']['sms']['message'] = document['messages']['sms']['message']
        customerestimateconfirmation['messages']['sms']['uuid'] = document['messages']['sms']['uuid']
        customerestimateconfirmation['messages']['letter']['message'] = document['messages']['letter']['message']
        customerestimateconfirmation['messages']['letter']['uuid'] = document['messages']['letter']['uuid']
        customerestimateconfirmation = {'customerestimateconfirmation' :customerestimateconfirmation}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return customerestimateconfirmation

