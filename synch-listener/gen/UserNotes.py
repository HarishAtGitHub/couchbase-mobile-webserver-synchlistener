import re
from Base import BaseCRUDObjects,AutoVivification

class UserNotes(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/users/{userId}/usernotes'
        return

    def postParams(self, document):
        url = '/api/v1/users/{userId}/usernotes'
        note = AutoVivification()
        userId = document['userId']
        new_user_note['communicationsnote']['title'] = document['communicationsnote']['title']
        new_user_note['communicationsnote']['note'] = document['communicationsnote']['note']
        note = {'note' :note}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return note

    def putParams(self, document):
        url = '/api/v1/users/{userId}/usernotes/{id}'
        note = AutoVivification()
        userId = document['userId']
        id = document['id']
        new_user_note['communicationsnote']['title'] = document['communicationsnote']['title']
        new_user_note['communicationsnote']['note'] = document['communicationsnote']['note']
        note = {'note' :note}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return note

    def deleteParams(self, document):
        url = '/api/v1/users/{userId}/usernotes/{id}'
        userId = document['userId']
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

    def getParams(self, document):
        url = '/api/v1/users/{userId}/usernotes/{noteId}'
        return

