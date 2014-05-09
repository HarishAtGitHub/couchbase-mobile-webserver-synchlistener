import re
from Base import BaseCRUDObjects,AutoVivification

class PrintAndPostCoveringLetter(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/printandpostcoveringletters'
        return

    def postParams(self, document):
        url = '/api/v1/printandpostcoveringletters'
        customcertificate = AutoVivification()
        customcertificate['message'] = document['message']
        customcertificate['uuid'] = document['uuid']
        customcertificate = {'customcertificate' :customcertificate}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return customcertificate

