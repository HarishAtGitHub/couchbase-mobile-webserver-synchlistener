import re
from Base import BaseCRUDObjects,AutoVivification

class Jobdescriptions(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/jobdescriptions'
        return

    def postParams(self, document):
        url = '/api/v1/jobdescriptions'
        jobdescription = AutoVivification()
        jobdescription['description'] = document['descriptionText']
        jobdescription['timetocomplete'] = document['timetocomplete']
        jobdescription['price'] = document['price']
        jobdescription['appearincustomerlogin'] = document['appearincustomerlogin']
        jobdescription['appearinwebbooking'] = document['appearinwebbooking']
        jobdescription['jobcolor'] = document['jobcolor']
        jobdescription['uuid'] = document['uuid']
        jobdescription['order'] = document['order']
        jobdescription = {'jobdescription' :jobdescription}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return jobdescription

    def putParams(self, document):
        url = '/api/v1/jobdescriptions/{id}'
        jobdescription = AutoVivification()
        id = document['id']
        jobdescription['description'] = document['descriptionText']
        jobdescription['timetocomplete'] = document['timetocomplete']
        jobdescription['price'] = document['price']
        jobdescription['appearincustomerlogin'] = document['appearincustomerlogin']
        jobdescription['appearinwebbooking'] = document['appearinwebbooking']
        jobdescription['jobcolor'] = document['jobcolor']
        jobdescription['order'] = document['order']
        jobdescription = {'jobdescription' :jobdescription}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return jobdescription

    def deleteParams(self, document):
        url = '/api/v1/jobdescriptions/{id}'
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

    def getParams(self, document):
        url = '/api/v1/jobdescriptions/{jobDescriptionId}'
        return

