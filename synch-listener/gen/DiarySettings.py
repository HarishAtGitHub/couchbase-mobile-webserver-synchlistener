import re
from Base import BaseCRUDObjects,AutoVivification

class DiarySettings(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/diarysettings'
        return

    def postParams(self, document):
        url = '/api/v1/diarysettings'
        diarysettings = AutoVivification()
        diarysettings['messages']['default']['value'] = document['messages']['default']['value']
        diarysettings['messages']['default']['uuid'] = document['messages']['default']['uuid']
        diarysettings['messages']['abortedevents']['value'] = document['messages']['abortedevents']['value']
        diarysettings['messages']['abortedevents']['uuid'] = document['messages']['abortedevents']['uuid']
        diarysettings['messages']['rejectedevents']['value'] = document['messages']['rejectedevents']['value']
        diarysettings['messages']['rejectedevents']['uuid'] = document['messages']['rejectedevents']['uuid']
        diarysettings['messages']['noaccessevents']['value'] = document['messages']['noaccessevents']['value']
        diarysettings['messages']['noaccessevents']['uuid'] = document['messages']['noaccessevents']['uuid']
        diarysettings = {'diarysettings' :diarysettings}

        path = url
        url_params = re.findall('\{([A-Za-z0-9]+)\}',path)
        if url_params:
            for url_param  in url_params :
                path = path.replace('{' + url_param + '}',str(eval(url_param)))
        self.url = path

        return diarysettings

