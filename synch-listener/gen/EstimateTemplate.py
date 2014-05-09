import re
from Base import BaseCRUDObjects,AutoVivification

class EstimateTemplate(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/estimatetemplates'
        return

    def postParams(self, document):
        url = '/api/v1/estimatetemplates'
        estimatetemplate = AutoVivification()
        estimatetemplate['description'] = document['descriptionText']
        estimatetemplate['colour'] = document['colour']
        estimatetemplate['uuid'] = document['uuid']
        estimatetemplate['order'] = document['order']
        estimatetemplate = {'estimatetemplate' :estimatetemplate}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return estimatetemplate

    def getParams(self, document):
        url = '/api/v1/estimatetemplates/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/estimatetemplates/{id}'
        estimatetemplate = AutoVivification()
        id = document['id']
        estimatetemplate['description'] = document['descriptionText']
        estimatetemplate['colour'] = document['colour']
        estimatetemplate['order'] = document['order']
        estimatetemplate = {'estimatetemplate' :estimatetemplate}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return estimatetemplate

    def deleteParams(self, document):
        url = '/api/v1/estimatetemplates/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

