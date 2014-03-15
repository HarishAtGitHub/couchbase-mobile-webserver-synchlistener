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
    
    
