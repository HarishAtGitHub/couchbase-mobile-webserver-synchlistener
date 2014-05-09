import re
from Base import BaseCRUDObjects,AutoVivification

class NewCompany(BaseCRUDObjects):
    def postParams(self, document):
        url = '/api/v1/companies'
        company = AutoVivification()
        company['contacts']['companyname'] = document['contacts']['companyname']
        company['addressline1'] = document['addressline1']
        company['addressline2'] = document['addressline2']
        company['town'] = document['town']
        company['county'] = document['county']
        company['postcode'] = document['postcode']
        company['contacts']['companylandline']['companylandline'] = document['contacts']['companylandline']['companylandline']
        company['contacts']['contactsemail']['emailaddress'] = document['contacts']['contactsemail']['emailaddress']
        company['optionalcontacts']['name'] = document['optionalcontacts']['name']
        company['optionalcontacts']['surname'] = document['optionalcontacts']['surname']
        company['optionalcontacts']['position'] = document['optionalcontacts']['position']
        company['contacts']['contactstelephone'][0]['telephonenumber'] = document['contacts']['contactstelephone'][0]['telephonenumber']
        company['contacts']['contactstelephone'][1]['telephonenumber'] = document['contacts']['contactstelephone'][1]['telephonenumber']
        company['optionalcontacts']['contactsemail']['emailaddress'] = document['optionalcontacts']['contactsemail']['emailaddress']
        company['settingsAdvertisingsid'] = document['settingsAdvertisingsid']
        company['uuid'] = document['uuid']
        company = {'company' :company}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return company

