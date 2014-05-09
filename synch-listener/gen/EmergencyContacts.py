import re
from Base import BaseCRUDObjects,AutoVivification

class EmergencyContacts(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/users/{id}/emergencycontacts'
        return

    def postParams(self, document):
        url = '/api/v1/users/{id}/emergencycontacts'
        emergencycontact = AutoVivification()
        id = document['id']
        emergencycontact['name'] = document['name']
        emergencycontact['surname'] = document['surname']
        emergencycontact['email'] = document['email']
        emergencycontact['telephone'] = document['telephone']
        emergencycontact['mobile'] = document['mobile']
        emergencycontact['relationship'] = document['relationship']
        emergencycontact['addressline1'] = document['addressline1']
        emergencycontact['addressline2'] = document['addressline2']
        emergencycontact['addressline3'] = document['addressline3']
        emergencycontact['town'] = document['town']
        emergencycontact['country'] = document['country']
        emergencycontact['postcode'] = document['postcode']
        emergencycontact = {'emergencycontact' :emergencycontact}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return emergencycontact

    def getParams(self, document):
        url = '/api/v1/users/{id}/emergencycontacts/{contactId}'
        return

    def putParams(self, document):
        url = '/api/v1/users/{id}/emergencycontacts/{contactId}'
        emergencycontact = AutoVivification()
        id = document['id']
        contactId = document['contactId']
        emergencycontact['name'] = document['name']
        emergencycontact['surname'] = document['surname']
        emergencycontact['email'] = document['email']
        emergencycontact['telephone'] = document['telephone']
        emergencycontact['mobile'] = document['mobile']
        emergencycontact['relationship'] = document['relationship']
        emergencycontact['addressline1'] = document['addressline1']
        emergencycontact['addressline2'] = document['addressline2']
        emergencycontact['addressline3'] = document['addressline3']
        emergencycontact['town'] = document['town']
        emergencycontact['country'] = document['country']
        emergencycontact['postcode'] = document['postcode']
        emergencycontact = {'emergencycontact' :emergencycontact}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return emergencycontact

    def deleteParams(self, document):
        url = '/api/v1/users/{id}/emergencycontacts/{contactId}'
        id = document['id']
        contactId = document['contactId']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

