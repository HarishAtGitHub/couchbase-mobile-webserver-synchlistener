import re
from Base import BaseCRUDObjects,AutoVivification

class SiteArrivalQuestions(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/sitearrivalquestions'
        return

    def postParams(self, document):
        url = '/api/v1/sitearrivalquestions'
        sitearrivalquestion = AutoVivification()
        sitearrivalquestion['questiondescription'] = document['questiondescriptionText']
        sitearrivalquestion['questionhelptext'] = document['questionhelptext']
        sitearrivalquestion['questionrequired'] = document['questionrequired']
        sitearrivalquestion['questiontype'] = document['questiontype']
        sitearrivalquestion['options'] = document['options']
        sitearrivalquestion['uuid'] = document['uuid']
        sitearrivalquestion['order'] = document['order']
        sitearrivalquestion = {'sitearrivalquestion' :sitearrivalquestion}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return sitearrivalquestion

    def getParams(self, document):
        url = '/api/v1/sitearrivalquestions/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/sitearrivalquestions/{id}'
        sitearrivalquestion = AutoVivification()
        id = document['id']
        sitearrivalquestion['questiondescription'] = document['questiondescriptionText']
        sitearrivalquestion['questionhelptext'] = document['questionhelptext']
        sitearrivalquestion['questionrequired'] = document['questionrequired']
        sitearrivalquestion['questiontype'] = document['questiontype']
        sitearrivalquestion['options'] = document['options']
        sitearrivalquestion = {'sitearrivalquestion' :sitearrivalquestion}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return sitearrivalquestion

    def deleteParams(self, document):
        url = '/api/v1/sitearrivalquestions/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

