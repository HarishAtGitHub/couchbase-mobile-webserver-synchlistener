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
       
       
CouchBase SynchGateway :
========================

      1) Download the deb package from http://www.couchbase.com/download#cb-mobile
      2) sudo dpkg -i <package name>
      3) To start SychGateway Do
         $ /opt/couchbase-sync-gateway/bin/sync_gateway
         Now the synch gateway would have started in port 4985
      Certain things to note while running this command 
      
SynchGateway  Options :

     -adminInterface="127.0.0.1:4985": Address to bind admin interface to
     -bucket="sync_gateway": Name of bucket
     -configServer="": URL of server that can return database configs
     -dbname="": Name of CouchDB database (defaults to name of bucket)
     -deploymentID="": Customer/project identifier for stats reporting
     -interface=":4984": Address to bind to
     -log="": Log keywords, comma separated
     -personaOrigin="": Base URL that clients use to connect to the server
     -pool="default": Name of pool
     -pretty=false: Pretty-print JSON responses
     -profileInterface="": Address to bind profile interface to
     -url="walrus:": Address of Couchbase server
     -verbose=false: Log more info about requests


How to start ? :
==============

-> Start Couch Base server

-> Enable beer-sample bucket for just trying out

-> Start Couch Base sych gateway 

        $ /opt/couchbase-sync-gateway/bin/sync_gateway -url="htt//localhost:8091" -bucket="beer-sample"
        
        According to docs synch gateway does not allow anonymous access  
        http://docs.couchbase.com/sync-gateway/#managing-guest-access
        so enable guest access for the time being using
        curl -X PUT localhost:4985/beer-sample/_user/GUEST --data    '{"disabled":false, "admin_channels":["public"]}'
        
-> Now since the synch gateway is up now , you can query for data using api defined for synch gateway

        http://docs.couchbase.com/sync-gateway/#sync-rest-api
        for example http://localhost:4984/beer-sample/_changes?feed=continuous&heartbeat=22924&style=all_docs&since=public:1
        
