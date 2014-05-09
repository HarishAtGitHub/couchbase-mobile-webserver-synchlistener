import re
from Base import BaseCRUDObjects,AutoVivification

class CertificateQuestions(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/customcertificates/{customCertificateId}/certificatequestions'
        return

    def postParams(self, document):
        url = '/api/v1/customcertificates/{customCertificateId}/certificatequestions'
        certificatequestion = AutoVivification()
        customCertificateId = document['customCertificateId']
        certificatequestion['questiondescription'] = document['questiondescriptionText']
        certificatequestion['questiontype'] = document['questiontype']
        certificatequestion['questionhelptext'] = document['questionhelptext']
        certificatequestion['settingscertificateid'] = document['settingscertificateid']
        certificatequestion['uuid'] = document['uuid']
        certificatequestion['order'] = document['order']
        certificatequestion['questionrequired'] = document['questionrequired']
        certificatequestion['questionOptions'] = document['questionOptions']
        certificatequestion = {'certificatequestion' :certificatequestion}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return certificatequestion

    def getParams(self, document):
        url = '/api/v1/customcertificates/{customCertificateId}/certificatequestions/{id}'
        return

    def putParams(self, document):
        url = '/api/v1/customcertificates/{customCertificateId}/certificatequestions/{id}'
        certificatequestion = AutoVivification()
        customCertificateId = document['customCertificateId']
        id = document['id']
        certificatequestion['questiondescription'] = document['questiondescriptionText']
        certificatequestion['questiontype'] = document['questiontype']
        certificatequestion['questionhelptext'] = document['questionhelptext']
        certificatequestion['questionId'] = document['questionId']
        certificatequestion['questionrequired'] = document['questionrequired']
        certificatequestion['questionOptions'] = document['questionOptions']
        certificatequestion = {'certificatequestion' :certificatequestion}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return certificatequestion

    def deleteParams(self, document):
        url = '/api/v1/customcertificates/{customCertificateId}/certificatequestions/{id}'
        customCertificateId = document['customCertificateId']
        id = document['id']

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return 

