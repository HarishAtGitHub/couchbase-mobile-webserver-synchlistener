import re
from Base import BaseCRUDObjects,AutoVivification

class EngineerEmailJobSheetMessage(BaseCRUDObjects):
    def postParams(self, document):
        url = '/api/v1/engineeremailjobsheetmessages'
        engineeremailjobsheetmessage = AutoVivification()
        engineeremailjobsheetmessage['subject'] = document['subject']
        engineeremailjobsheetmessage['message'] = document['message']
        engineeremailjobsheetmessage['uuid'] = document['uuid']
        engineeremailjobsheetmessage = {'engineeremailjobsheetmessage' :engineeremailjobsheetmessage}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return engineeremailjobsheetmessage

