import sqlite3
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('conf/settings.conf')

conn = sqlite3.connect(config.get('db', 'dblocation'))
print "Opened database successfully";

conn.execute('''CREATE TABLE TRACKSEQNUMBER
       (
        CHANNELNAME TEXT PRIMARY KEY    NOT NULL,
        LASTSEQUENCENUMBER INT     NOT NULL,
        UNIQUE (CHANNELNAME)
       );''')
print "Table created successfully";

conn.close()

