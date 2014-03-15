NOTE :
======

     1) The step in https://github.com/HarishAtGitHub/couchbase-learning/blob/master/README.md to enable Guest access is important for synch gateway to access public channels 
     2) The most important part of config.json is the "sync" part . This synch function says which channel to use .
        without this it cannot access the documents in the configured buckets .You can try by removing this and try accessing  you will get something like 
        
        {"rows":[
                ],
         "total_rows":3,"update_seq":3
        }
        
        But if you have that synch function you can even see the documents as follows 
        
        {
    "rows": [
        {
            "id": "defauldoc1",
            "key": "defauldoc1",
            "value": {
                "rev": "1-32a47328ef0da54672a340b55855cbe9"
            },
            "doc": {
                "_id": "defauldoc1",
                "_rev": "1-32a47328ef0da54672a340b55855cbe9",
                "click": "I am default doc1",
                "new in 2.0": "There r no fields"
            }
        },
        {
            "id": "harish",
            "key": "harish",
            "value": {
                "rev": "1-1d7a1a352c0abb293fdd16883ef6985b"
            },
            "doc": {
                "_id": "harish",
                "_rev": "1-1d7a1a352c0abb293fdd16883ef6985b",
                "click": "to edit",
                "new in 2.0": "there are no reserved field names"
            }
        },
        {
            "id": "harish1",
            "key": "harish1",
            "value": {
                "rev": "1-7ee3672a7a34af8d4c3e5384b9678ae8"
            },
            "doc": {
                "_id": "harish1",
                "_rev": "1-7ee3672a7a34af8d4c3e5384b9678ae8",
                "click": "I am harish1",
                "new in 2.0": "This is a sample"
            }
        }
    ],
    "total_rows": 3,
    "update_seq": 3
    }
    
    
    
### Difference between http://localhost:4984/default/_all_docs and http://localhost:4984/default/_all_docs?include_docs=true


1) The first url only brings document details with the revision id's 

2) if you want the document's content also , then use second url 



### What happens if after starting a synch gateway , I go and edit a document directly in  couchbase serve in UI ?

That is not picked up by the synch gateway . You can check by creating one directly in UI . But that will be picked up next time when I restart the synch gateway .
And you can see additional information seen in the doc in couch base server
