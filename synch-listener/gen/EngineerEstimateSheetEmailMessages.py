import re
from Base import BaseCRUDObjects,AutoVivification

class EngineerEstimateSheetEmailMessages(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/engineerestimatesheetemailmessages'
        return

    def postParams(self, document):
        url = '/api/v1/engineerestimatesheetemailmessages'
        engineerestimatesheetemailmessage = AutoVivification()
        engineerestimatesheetemailmessage['subject'] = document['subject']
        engineerestimatesheetemailmessage['message'] = document['message']
        engineerestimatesheetemailmessage = {'engineerestimatesheetemailmessage' :engineerestimatesheetemailmessage}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return engineerestimatesheetemailmessage

