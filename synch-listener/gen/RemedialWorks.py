import re
from Base import BaseCRUDObjects,AutoVivification

class RemedialWorks(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/remedialworks'
        return

    def postParams(self, document):
        url = '/api/v1/remedialworks'
        remedialworks = AutoVivification()
        remedialworks['value'] = document['value']
        remedialworks['uuid'] = document['uuid']
        remedialworks = {'remedialworks' :remedialworks}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return remedialworks

