import re
from Base import BaseCRUDObjects,AutoVivification

class EstimateEmailMessage(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/estimateemailmessages'
        return

    def postParams(self, document):
        url = '/api/v1/estimateemailmessages'
        estimateemailmessage = AutoVivification()
        estimateemailmessage['subject'] = document['subject']
        estimateemailmessage['message'] = document['message']
        estimateemailmessage['uuid'] = document['uuid']
        estimateemailmessage = {'estimateemailmessage' :estimateemailmessage}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return estimateemailmessage

