import re
from Base import BaseCRUDObjects,AutoVivification

class Newvehicles(BaseCRUDObjects):
    def getParams(self, document):
        url = '/api/v1/newvehicles/{id}'
        return

