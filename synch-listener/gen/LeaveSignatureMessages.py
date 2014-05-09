import re
from Base import BaseCRUDObjects,AutoVivification

class LeaveSignatureMessages(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/leavesignaturemessages'
        return

    def postParams(self, document):
        url = '/api/v1/leavesignaturemessages'
        leavesignaturemessage = AutoVivification()
        leavesignaturemessage['value'] = document['value']
        leavesignaturemessage['uuid'] = document['uuid']
        leavesignaturemessage['setup'] = document['setup']
        leavesignaturemessage = {'leavesignaturemessage' :leavesignaturemessage}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return leavesignaturemessage

