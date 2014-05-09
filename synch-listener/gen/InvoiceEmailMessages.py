import re
from Base import BaseCRUDObjects,AutoVivification

class InvoiceEmailMessages(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/invoiceemailmessages'
        return

    def postParams(self, document):
        url = '/api/v1/invoiceemailmessages'
        settingsemailmessage = AutoVivification()
        settingsemailmessage['subject'] = document['subject']
        settingsemailmessage['message'] = document['message']
        settingsemailmessage['uuid'] = document['uuid']
        settingsemailmessage = {'settingsemailmessage' :settingsemailmessage}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return settingsemailmessage

