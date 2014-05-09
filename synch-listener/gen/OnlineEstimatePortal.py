import re
from Base import BaseCRUDObjects,AutoVivification

class OnlineEstimatePortal(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/onlineestimateportals'
        return

    def postParams(self, document):
        url = '/api/v1/onlineestimateportals'
        onlineestimateportal = AutoVivification()
        onlineestimateportal['messages']['enableportal']['value'] = document['messages']['enableportal']['value']
        onlineestimateportal['messages']['enableportal']['uuid'] = document['messages']['enableportal']['uuid']
        onlineestimateportal['messages']['attachpdf']['value'] = document['messages']['attachpdf']['value']
        onlineestimateportal['messages']['attachpdf']['uuid'] = document['messages']['attachpdf']['uuid']
        onlineestimateportal['messages']['declaration']['value'] = document['messages']['declaration']['value']
        onlineestimateportal['messages']['declaration']['uuid'] = document['messages']['declaration']['uuid']
        onlineestimateportal = {'onlineestimateportal' :onlineestimateportal}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return onlineestimateportal

