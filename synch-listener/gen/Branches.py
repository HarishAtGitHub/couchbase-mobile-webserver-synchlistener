import re
from Base import BaseCRUDObjects,AutoVivification

class Branches(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/customers/{id}/branches'
        return

    def getParams(self, document):
        url = '/api/v1/customers/{id}/branches/{branchId}'
        return

