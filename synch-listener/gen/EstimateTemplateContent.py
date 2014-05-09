import re
from Base import BaseCRUDObjects,AutoVivification

class EstimateTemplateContent(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/estimatetemplates/{id}/templatecontents'
        return

    def postParams(self, document):
        url = '/api/v1/estimatetemplates/{id}/templatecontents'
        estimatetemplate = AutoVivification()
        id = document['id']
        estimatetemplate['subject'] = document['subject']
        estimatetemplate['message'] = document['message']
        estimatetemplate = {'estimatetemplate' :estimatetemplate}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return estimatetemplate

