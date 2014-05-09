import re
from Base import BaseCRUDObjects,AutoVivification

class Nominalgroups(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/nominalgroups'
        return

    def postParams(self, document):
        url = '/api/v1/nominalgroups'
        nominalgroup = AutoVivification()
        nominalgroup['description'] = document['descriptionText']
        nominalgroup['uuid'] = document['uuid']
        nominalgroup = {'nominalgroup' :nominalgroup}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return nominalgroup

    def putParams(self, document):
        url = '/api/v1/nominalgroups/{id}'
        nominalgroup = AutoVivification()
        id = document['id']
        nominalgroup['description'] = document['descriptionText']
        nominalgroup = {'nominalgroup' :nominalgroup}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return nominalgroup

    def deleteParams(self, document):
        url = '/api/v1/nominalgroups/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

    def getParams(self, document):
        url = '/api/v1/nominalgroups/{nominalGroupId}'
        return

