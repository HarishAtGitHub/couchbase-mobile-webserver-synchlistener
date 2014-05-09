import re
from Base import BaseCRUDObjects,AutoVivification

class UpdateCustomer(BaseCRUDObjects):
    def putParams(self, document):
        url = '/api/v1/customers/{id}'
        customertype = AutoVivification()
        id = document['id']
        customertype['settingsTitlesid'] = document['settingsTitlesid']
        customertype['name'] = document['name']
        customertype['surname'] = document['surname']
        customertype['telephonecountrycode'] = document['telephonecountrycode']
        customertype['mobilecountrycode'] = document['mobilecountrycode']
        customertype['mobile'] = document['mobile']
        customertype['email'] = document['email']
        customertype['postcode'] = document['postcode']
        customertype['addressline1'] = document['addressline1']
        customertype['addressline2'] = document['addressline2']
        customertype['addressline3'] = document['addressline3']
        customertype['town'] = document['town']
        customertype['county'] = document['county']
        customertype['settingsAdvertisingsid'] = document['settingsAdvertisingsid']
        customertype['settingsBuildingtypesid'] = document['settingsBuildingtypesid']
        customertype['vacantproperty'] = document['vacantproperty']
        customertype['thirdparty'] = document['thirdparty']
        customertype = {'customertype' :customertype}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return customertype

