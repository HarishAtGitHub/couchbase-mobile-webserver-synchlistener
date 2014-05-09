import re
from Base import BaseCRUDObjects,AutoVivification

class NoAccessMessages(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/noaccessmessages'
        return

    def postParams(self, document):
        url = '/api/v1/noaccessmessages'
        noaccessmessage = AutoVivification()
        noaccessmessage['setup'] = document['setup']
        noaccessmessage['messages']['email']['subject'] = document['messages']['email']['subject']
        noaccessmessage['messages']['email']['message'] = document['messages']['email']['message']
        noaccessmessage['messages']['email']['uuid'] = document['messages']['email']['uuid']
        noaccessmessage['messages']['sms']['message'] = document['messages']['sms']['message']
        noaccessmessage['messages']['sms']['uuid'] = document['messages']['sms']['uuid']
        noaccessmessage['messages']['wemail']['subject'] = document['messages']['wemail']['subject']
        noaccessmessage['messages']['wemail']['message'] = document['messages']['wemail']['message']
        noaccessmessage['messages']['wemail']['uuid'] = document['messages']['wemail']['uuid']
        noaccessmessage['messages']['wsms']['message'] = document['messages']['wsms']['message']
        noaccessmessage['messages']['wsms']['uuid'] = document['messages']['wsms']['uuid']
        noaccessmessage = {'noaccessmessage' :noaccessmessage}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return noaccessmessage

