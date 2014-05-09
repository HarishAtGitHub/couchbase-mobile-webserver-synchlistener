import re
from Base import BaseCRUDObjects,AutoVivification

class CustomerLoginEmailMessage(BaseCRUDObjects):
    def postParams(self, document):
        url = '/api/v1/customerloginemailmessages'
        customerloginemailmessage = AutoVivification()
        customerloginemailmessage['messages']['email']['subject'] = document['messages']['email']['subject']
        customerloginemailmessage['messages']['email']['message'] = document['messages']['email']['message']
        customerloginemailmessage['messages']['email']['uuid'] = document['messages']['email']['uuid']
        customerloginemailmessage = {'customerloginemailmessage' :customerloginemailmessage}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return customerloginemailmessage

