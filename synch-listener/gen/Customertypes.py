import re
from Base import BaseCRUDObjects,AutoVivification

class Customertypes(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/customertypes'
        return

    def postParams(self, document):
        url = '/api/v1/customertypes'
        customertype = AutoVivification()
        customertype['description'] = document['descriptionText']
        customertype['customerdescription'] = document['customerdescriptionText']
        customertype['companynamerequired'] = document['companynamerequired']
        customertype['allowforbranches'] = document['allowforbranches']
        customertype['typeofjobaddress'] = document['typeofjobaddress']
        customertype['uuid'] = document['uuid']
        customertype['order'] = document['order']
        customertype = {'customertype' :customertype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return customertype

    def putParams(self, document):
        url = '/api/v1/customertypes/{id}'
        customertype = AutoVivification()
        id = document['id']
        customertype['description'] = document['descriptionText']
        customertype['customerdescription'] = document['customerdescriptionText']
        customertype['companynamerequired'] = document['companynamerequired']
        customertype['allowforbranches'] = document['allowforbranches']
        customertype['typeofjobaddress'] = document['typeofjobaddress']
        customertype['uuid'] = document['uuid']
        customertype['order'] = document['order']
        customertype = {'customertype' :customertype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return customertype

    def deleteParams(self, document):
        url = '/api/v1/customertypes/{id}/{mergeid}'
        id = document['id']
        mergeid = document['mergeid']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

