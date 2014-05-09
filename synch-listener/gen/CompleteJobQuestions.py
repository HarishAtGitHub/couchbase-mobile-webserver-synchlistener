import re
from Base import BaseCRUDObjects,AutoVivification

class CompleteJobQuestions(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/completejobquestions'
        return

    def postParams(self, document):
        url = '/api/v1/completejobquestions'
        completejobquestion = AutoVivification()
        completejobquestion['questiondescription'] = document['questiondescriptionText']
        completejobquestion['questionhelptext'] = document['questionhelptext']
        completejobquestion['questionrequired'] = document['questionrequired']
        completejobquestion['questiontype'] = document['questiontype']
        completejobquestion['options'] = document['options']
        completejobquestion['uuid'] = document['uuid']
        completejobquestion['order'] = document['order']
        completejobquestion = {'completejobquestion' :completejobquestion}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return completejobquestion

    def getParams(self, document):
        url = '/api/v1/completejobquestions/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/completejobquestions/{id}'
        completejobquestion = AutoVivification()
        id = document['id']
        completejobquestion['questiondescription'] = document['questiondescriptionText']
        completejobquestion['questionhelptext'] = document['questionhelptext']
        completejobquestion['questionrequired'] = document['questionrequired']
        completejobquestion['questiontype'] = document['questiontype']
        completejobquestion['options'] = document['options']
        completejobquestion = {'completejobquestion' :completejobquestion}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return completejobquestion

    def deleteParams(self, document):
        url = '/api/v1/completejobquestions/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

