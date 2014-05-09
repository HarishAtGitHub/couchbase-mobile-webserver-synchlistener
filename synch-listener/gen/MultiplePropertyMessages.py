import re
from Base import BaseCRUDObjects,AutoVivification

class MultiplePropertyMessages(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/servicereminders/{id}/multiplepropertymessages'
        return

    def postParams(self, document):
        url = '/api/v1/servicereminders/{id}/multiplepropertymessages'
        followupmessages = AutoVivification()
        id = document['id']
        ['messages']['email']['subject'] = document['messages']['email']['subject']
        ['messages']['email']['message'] = document['messages']['email']['message']
        ['messages']['sms']['message'] = document['messages']['sms']['message']
        ['messages']['letter']['message'] = document['messages']['letter']['message']
        followupmessages['name'] = document['name']
        followupmessages['period'] = document['period']
        followupmessages['messages']['email']['subject'] = document['messages']['email']['subject']
        followupmessages['messages']['email']['message'] = document['messages']['email']['message']
        followupmessages['messages']['sms']['message'] = document['messages']['sms']['message']
        followupmessages['messages']['letter']['message'] = document['messages']['letter']['message']
        followupmessages = {'followupmessages' :followupmessages}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return followupmessages

