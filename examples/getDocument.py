from couchbase import Couchbase
from pprint import pprint
client = Couchbase.connect(bucket='test1',host='localhost',port=8091,password='ebullient')
result = client.get('doc1')
pprint (result.value , indent=4)


