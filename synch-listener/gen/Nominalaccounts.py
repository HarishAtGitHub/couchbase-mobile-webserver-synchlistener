import re
from Base import BaseCRUDObjects,AutoVivification

class Nominalaccounts(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/nominalgroups/{nominalGroupId}/nominalaccounts'
        return

    def postParams(self, document):
        url = '/api/v1/nominalgroups/{nominalGroupId}/nominalaccounts'
        nominalaccounttype = AutoVivification()
        nominalGroupId = document['nominalGroupId']
        nominalaccounttype['description'] = document['descriptionText']
        nominalaccounttype['uuid'] = document['uuid']
        nominalaccounttype = {'nominalaccounttype' :nominalaccounttype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return nominalaccounttype

    def getParams(self, document):
        url = '/api/v1/nominalgroups/{nominalGroupId}/nominalaccounts/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/nominalgroups/{nominalGroupId}/nominalaccounts/{id}'
        nominalaccounttype = AutoVivification()
        nominalGroupId = document['nominalGroupId']
        id = document['id']
        nominalaccounttype['description'] = document['descriptionText']
        nominalaccounttype = {'nominalaccounttype' :nominalaccounttype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return nominalaccounttype

    def deleteParams(self, document):
        url = '/api/v1/nominalgroups/{nominalGroupId}/nominalaccounts/{id}'
        nominalGroupId = document['nominalGroupId']
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

