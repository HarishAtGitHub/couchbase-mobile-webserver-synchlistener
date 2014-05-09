import re
from Base import BaseCRUDObjects,AutoVivification

class Apikey(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/getKey'
        return

