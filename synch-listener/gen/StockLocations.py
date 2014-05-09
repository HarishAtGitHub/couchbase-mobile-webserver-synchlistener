import re
from Base import BaseCRUDObjects,AutoVivification

class StockLocations(BaseCRUDObjects):
    def getParams_list(self, document):
        url = '/api/v1/stocklocations'
        return

