import re
from Base import BaseCRUDObjects,AutoVivification

class CustomiseMiniApp(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/customerloginemailmessages'
        return

    def getParams_list(self, document):
        url = '/api/v1/customiseminiapps'
        return

    def postParams(self, document):
        url = '/api/v1/customiseminiapps'
        customiseminiapp = AutoVivification()
        customiseminiapp['emailnotification'] = document['emailnotification']
        customiseminiapp['messages']['email']['subject'] = document['messages']['email']['subject']
        customiseminiapp['messages']['email']['message'] = document['messages']['email']['message']
        customiseminiapp['messages']['email']['uuid'] = document['messages']['email']['uuid']
        customiseminiapp = {'customiseminiapp' :customiseminiapp}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return customiseminiapp

