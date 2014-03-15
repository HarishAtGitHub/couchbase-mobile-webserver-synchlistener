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
And you can see additional information seen in the doc in couch base server.
This is the area where Couch Mobile client comes in .Couch base mobile client writes to synch gateway and synch gateway takes care of synching to couchbase server . Writing to synch gateway manages all the problems . Or to be exact it is writing VIA synch gateway .

### if after starting a synch gateway , I go and edit a document directly in  couchbase serve in UI. Now the doc only has the value that we gave . But now when we restart synch gateway I find that the doc in couchbase server is modified to have so much other meta data . Is this the expected behaviour ?

Yes there are a lot of metadata .

I gave only 
{
  "click": "to edit",
  "new in 2.0": "there are no reserved field names"
}

But after synch gateway restart I find the doc having the following 
{
  "_id": "check2",
  "_rev": "1-1d7a1a352c0abb293fdd16883ef6985b",
  "_sync": {
    "rev": "1-1d7a1a352c0abb293fdd16883ef6985b",
    "sequence": 5,
    "history": {
      "revs": [
        "1-1d7a1a352c0abb293fdd16883ef6985b"
      ],
      "parents": [
        -1
      ],
      "bodies": [
        ""
      ],
      "channels": [
        [
          "public"
        ]
      ]
    },
    "channels": {
      "public": null
    },
    "time_saved": "0001-01-01T00:00:00Z"
  },
  "click": "to edit",
  "new in 2.0": "there are no reserved field names"
}


I am not sure , may be to relieve of this so called problem , they have the concept of bucket shadowing (introduced jan 2014)
https://github.com/couchbase/sync_gateway/wiki/Bucket-Shadowing

