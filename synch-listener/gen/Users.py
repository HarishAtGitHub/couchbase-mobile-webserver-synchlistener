import re
from Base import BaseCRUDObjects,AutoVivification

class Users(BaseCRUDObjects):
    def postParams(self, document):
        url = '/api/v1/users'
        newuser = AutoVivification()
        newuser['name'] = document['name']
        newuser['surname'] = document['surname']
        newuser['mobile'] = document['mobile']
        newuser['telephone'] = document['telephone']
        newuser['email'] = document['email']
        newuser['nationalinsurance'] = document['nationalinsurance']
        newuser['addressline1'] = document['addressline1']
        newuser['addressline2'] = document['addressline2']
        newuser['addressline3'] = document['addressline3']
        newuser['town'] = document['town']
        newuser['county'] = document['county']
        newuser['postcode'] = document['postcode']
        newuser['appearondiary'] = document['appearondiary']
        newuser['username'] = document['username']
        newuser['password'] = document['password']
        newuser['passwordsalt'] = document['passwordsalt']
        newuser['settingsSecurityrolesid'] = document['settingsSecurityrolesid']
        newuser['settingsUsergroupsid'] = document['settingsUsergroupsid']
        newuser['usertype'] = document['usertype']
        newuser['settingsClientbranchesid'] = document['settingsClientbranchesid']
        newuser = {'newuser' :newuser}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return newuser

    def getParams(self, document):
        url = '/api/v1/users/{id}'
        return

    def getParams_list(self, document):
        url = '/api/v1/users/{id}/businessdetails'
        return

    def putParams(self, document):
        url = '/api/v1/users/{id}/businessdetails'
        user = AutoVivification()
        id = document['id']
        user['branch'] = document['branch']
        user['usergroup'] = document['usergroup']
        user['appearondiary'] = document['appearondiary']
        user['colourondiary'] = document['colourondiary']
        user['employmenttype'] = document['employmenttype']
        user['datejoined'] = document['datejoined']
        user = {'user' :user}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return user

    def getParams_list(self, document):
        url = '/api/v1/users/{id}/logindetails'
        return

    def putParams(self, document):
        url = '/api/v1/users/{id}/logindetails'
        user = AutoVivification()
        id = document['id']
        user['username'] = document['username']
        user['status'] = document['status']
        user = {'user' :user}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return user

    def getParams_list(self, document):
        url = '/api/v1/users/{id}/officialnumbers'
        return

    def putParams(self, document):
        url = '/api/v1/users/{id}/officialnumbers'
        user = AutoVivification()
        id = document['id']
        user['NI'] = document['NI']
        user['gassafeid'] = document['gassafeid']
        user = {'user' :user}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return user

    def getParams_list(self, document):
        url = '/api/v1/users/{id}/personaldetails'
        return

    def putParams(self, document):
        url = '/api/v1/users/{id}/personaldetails'
        user = AutoVivification()
        id = document['id']
        user['name'] = document['name']
        user['surname'] = document['surname']
        user['profileimage'] = document['profileimage']
        user['email'] = document['email']
        user['telephone'] = document['telephone']
        user['mobile'] = document['mobile']
        user['address1'] = document['address1']
        user['address2'] = document['address2']
        user['town'] = document['town']
        user['country'] = document['country']
        user['postcode'] = document['postcode']
        user['signature'] = document['signature']
        user = {'user' :user}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return user

