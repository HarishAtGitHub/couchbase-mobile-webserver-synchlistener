from couchbase import Couchbase
client = Couchbase.connect(bucket='test1',host='localhost',port=8091,password='ebullient')
client.set('doc1','doc1value')

