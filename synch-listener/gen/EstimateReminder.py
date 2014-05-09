import re
from Base import BaseCRUDObjects,AutoVivification

class EstimateReminder(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/estimatereminders'
        return

    def postParams(self, document):
        url = '/api/v1/estimatereminders'
        estimatereminder = AutoVivification()
        estimatereminder['automaticallysend'] = document['automaticallysend']
        estimatereminder['messages']['email']['uuid'] = document['messages']['email']['uuid']
        estimatereminder['messages']['email']['subject'] = document['messages']['email']['subject']
        estimatereminder['messages']['email']['message'] = document['messages']['email']['message']
        estimatereminder['messages']['sms']['uuid'] = document['messages']['sms']['uuid']
        estimatereminder['messages']['sms']['message'] = document['messages']['sms']['message']
        estimatereminder = {'estimatereminder' :estimatereminder}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return estimatereminder

