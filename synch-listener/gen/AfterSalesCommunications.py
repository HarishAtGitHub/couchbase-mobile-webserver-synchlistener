import re
from Base import BaseCRUDObjects,AutoVivification

class AfterSalesCommunications(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/aftersalescommunications'
        return

    def postParams(self, document):
        url = '/api/v1/aftersalescommunications'
        aftersalescommunication = AutoVivification()
        aftersalescommunication['messages']['email']['subject'] = document['messages']['email']['subject']
        aftersalescommunication['messages']['email']['message'] = document['messages']['email']['message']
        aftersalescommunication['messages']['email']['uuid'] = document['messages']['email']['uuid']
        aftersalescommunication['messages']['sms']['message'] = document['messages']['sms']['message']
        aftersalescommunication['messages']['sms']['uuid'] = document['messages']['sms']['uuid']
        aftersalescommunication['messages']['letter']['message'] = document['messages']['letter']['message']
        aftersalescommunication['messages']['letter']['uuid'] = document['messages']['letter']['uuid']
        aftersalescommunication = {'aftersalescommunication' :aftersalescommunication}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return aftersalescommunication

