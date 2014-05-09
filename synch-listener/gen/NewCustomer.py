import re
from Base import BaseCRUDObjects,AutoVivification

class NewCustomer(BaseCRUDObjects):
    def postParams(self, document):
        url = '/api/v1/customers'
        customertype = AutoVivification()
        customertype['contacts']['settingsTitlesid'] = document['contacts']['settingsTitlesid']
        customertype['contacts']['name'] = document['contacts']['name']
        customertype['contacts']['surname'] = document['contacts']['surname']
        customertype['contacts']['contactstelephone'][0]['telephonenumber'] = document['contacts']['contactstelephone'][0]['telephonenumber']
        customertype['contacts']['contactstelephone'][1]['telephonenumber'] = document['contacts']['contactstelephone'][1]['telephonenumber']
        customertype['contacts']['contactsemail']['emailaddress'] = document['contacts']['contactsemail']['emailaddress']
        customertype['postcode'] = document['postcode']
        customertype['addressline1'] = document['addressline1']
        customertype['addressline2'] = document['addressline2']
        customertype['addressline3'] = document['addressline3']
        customertype['town'] = document['town']
        customertype['county'] = document['county']
        customertype['settingsAdvertisingsid'] = document['settingsAdvertisingsid']
        customertype['uuid'] = document['uuid']
        customertype = {'customertype' :customertype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return customertype

