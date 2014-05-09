import re
from Base import BaseCRUDObjects,AutoVivification

class LeaveJobQuestions(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/leavejobquestions'
        return

    def postParams(self, document):
        url = '/api/v1/leavejobquestions'
        leavejobquestion = AutoVivification()
        leavejobquestion['questiondescription'] = document['questiondescriptionText']
        leavejobquestion['questionhelptext'] = document['questionhelptext']
        leavejobquestion['questionrequired'] = document['questionrequired']
        leavejobquestion['questiontype'] = document['questiontype']
        leavejobquestion['options'] = document['options']
        leavejobquestion['uuid'] = document['uuid']
        leavejobquestion['order'] = document['order']
        leavejobquestion = {'leavejobquestion' :leavejobquestion}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return leavejobquestion

    def getParams(self, document):
        url = '/api/v1/leavejobquestions/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/leavejobquestions/{id}'
        leavejobquestion = AutoVivification()
        id = document['id']
        leavejobquestion['questiondescription'] = document['questiondescriptionText']
        leavejobquestion['questionhelptext'] = document['questionhelptext']
        leavejobquestion['questionrequired'] = document['questionrequired']
        leavejobquestion['questiontype'] = document['questiontype']
        leavejobquestion['options'] = document['options']
        leavejobquestion['order'] = document['order']
        leavejobquestion = {'leavejobquestion' :leavejobquestion}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return leavejobquestion

    def deleteParams(self, document):
        url = '/api/v1/leavejobquestions/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

