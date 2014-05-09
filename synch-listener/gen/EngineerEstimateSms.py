import re
from Base import BaseCRUDObjects,AutoVivification

class EngineerEstimateSms(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/engineerestimatesms'
        return

    def postParams(self, document):
        url = '/api/v1/engineerestimatesms'
        engineerestimatesms = AutoVivification()
        engineerestimatesms['messages'] = document['messages']
        engineerestimatesms['uuid'] = document['uuid']
        engineerestimatesms = {'engineerestimatesms' :engineerestimatesms}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return engineerestimatesms

