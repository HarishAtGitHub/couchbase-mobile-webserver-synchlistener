import re
from Base import BaseCRUDObjects,AutoVivification

class PurchaseOrderEmailMessage(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/purchaseorderemailmessages'
        return

    def postParams(self, document):
        url = '/api/v1/purchaseorderemailmessages'
        purchaseorderemailmessage = AutoVivification()
        purchaseorderemailmessage['subject'] = document['subject']
        purchaseorderemailmessage['message'] = document['message']
        purchaseorderemailmessage['uuid'] = document['uuid']
        purchaseorderemailmessage = {'purchaseorderemailmessage' :purchaseorderemailmessage}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return purchaseorderemailmessage

