import re
from Base import BaseCRUDObjects,AutoVivification

class CustomerTypes(BaseCRUDObjects):
    def getParams(self, document):
        url = '/api/v1/customertypes/{id}'
        return

