import sys
from couchbase import Couchbase
from couchbase.exceptions import CouchbaseError
try:
    client = Couchbase.connect(bucket='test1',host='localhost',port=8091,password='ebullient')
except CouchbaseError as e:
    print " Sorry , we could not create connection to bucket specified , due to " , e
else :
    print "Successfully made the connection to bucket "

try:
    client.delete('doc2')
except CouchbaseError as e :
    print "There was an error encountered while deleteing the given key ", e
except:
    print "Unexpected error has occured.", sys.exc_info()[0]
    raise
else :
    print "Successfully deleted the document"  
