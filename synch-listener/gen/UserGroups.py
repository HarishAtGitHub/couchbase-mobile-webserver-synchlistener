import re
from Base import BaseCRUDObjects,AutoVivification

class UserGroups(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/usergroups'
        return

    def postParams(self, document):
        url = '/api/v1/usergroups'
        usergroup = AutoVivification()
        usergroup['description'] = document['descriptionText']
        usergroup['uuid'] = document['uuid']
        usergroup['order'] = document['order']
        usergroup = {'usergroup' :usergroup}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return usergroup

    def getParams(self, document):
        url = '/api/v1/usergroups/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/usergroups/{id}'
        usergroup = AutoVivification()
        id = document['id']
        usergroup['description'] = document['descriptionText']
        usergroup['order'] = document['order']
        usergroup = {'usergroup' :usergroup}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return usergroup

    def deleteParams(self, document):
        url = '/api/v1/usergroups/{id}/{mergeid}'
        id = document['id']
        mergeid = document['mergeid']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

