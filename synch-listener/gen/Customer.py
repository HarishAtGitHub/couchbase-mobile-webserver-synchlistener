import re
from Base import BaseCRUDObjects,AutoVivification

class Customer(BaseCRUDObjects):
    def getParams(self, document):
        url = '/api/v1/customers/{id}'
        return

