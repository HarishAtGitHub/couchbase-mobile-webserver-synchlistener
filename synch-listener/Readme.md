step 1 : Fill the configuration file settings.conf in conf folder with appropriate values(see the example values for help)

step 2 : Run the DBTablecreator.py as (this will create a db with tables in it)

         python DBTablecreator.py
         
step 3 : start the couchbase server and synch gateway 
         you can use the conf file for synch gateway that is inside synchgateway folder with values changed
         
step 4 : start the synchlistner

         python synchlistener.py


To generate the stub files and see do : ( this fetches the api doc at the url specified and generates  the stub , so see to it that the internet is up , or else download the page and change reststub.py lines 93 and 94)

         cd src
         python reststubcreator.py



Requirements :

1) Install Logstash

      sudo pip install python-logstash

2) Install Python logstash formatter

      sudo pip install logstash_formatter

3) Install elastic search (we can also use embedded elastic search using logstash flat jar)
     wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.1.0.deb
     sudo dpkg -i <deb package fully>

     By default elastic search runs in http://localhost:9200/
     check if the access to the above url gives repsonse

**you have 2 options for analysing logs**

1) using kibana ( I personally prefer that as it is way ahead)

2) using default web ui

**using kibana**

     java -jar logstash-1.3.3-flatjar.jar agent -f conf/logstashkibana.conf -v -- web
     access web ui in http://localhost:9292/index.html#/dashboard/file/logstash.json
     
**using default web ui**

    java -jar logstash-1.1.0-monolithic.jar agent -f conf/logstash.conf -- web
    (Note that the location of log file is correct in conf/logstash.conf )
    access web ui in http://localhost:9292/


     
