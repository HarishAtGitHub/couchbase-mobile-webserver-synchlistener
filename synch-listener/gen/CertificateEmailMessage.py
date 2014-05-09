import re
from Base import BaseCRUDObjects,AutoVivification

class CertificateEmailMessage(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/certificateemailmessages'
        return

    def postParams(self, document):
        url = '/api/v1/certificateemailmessages'
        certificateemailmessage = AutoVivification()
        certificateemailmessage['subject'] = document['subject']
        certificateemailmessage['message'] = document['message']
        certificateemailmessage['uuid'] = document['uuid']
        certificateemailmessage = {'certificateemailmessage' :certificateemailmessage}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return certificateemailmessage

