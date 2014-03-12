couchbase-learning
==================

This repository has examples to start with couch base

Installation Procedure :

CouchBase Server : 
==================

       $ sudo apt-get install libssl0.9.8
       $ sudo dpkg -i couchbase-server-enterprise_2.5.0_x86_64_openssl098.deb
       $ sudo /etc/init.d/couchbase-server start
       
go to localhost:8091 and click set up 
Then now You will find a default bucket available .
So lets create bucket in UI. Now this bucket is empty. Lets add document. This can be done in UI .
But lets try programmatically . For that I need CouchBase client. Lets install it

CouchBase Python client :
=========================

       $ sudo apt-get install build-essential
       $ sudo apt-get install python-dev
       $ sudo pip install couchbase
       
Now try the examples
       
       

       

