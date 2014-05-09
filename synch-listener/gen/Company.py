import re
from Base import BaseCRUDObjects,AutoVivification

class Company(BaseCRUDObjects):
    def getParams(self, document):
        url = '/api/v1/companies/{id}'
        return

