from pyArango.connection import *

conn = Connection(arangoURL = 'http://vpsfree/arango', username="root", password="javornIk85", )

DB_NAME = "upracmeslovensko_dev"
COLLECTION_NAME = "texty_preklad"

if not conn.hasDatabase(DB_NAME):
    conn.createDatabase(name=DB_NAME)

db = conn[DB_NAME]

if not db.hasCollection(COLLECTION_NAME):
    collection = db.createCollection(name=COLLECTION_NAME)

collection = db[COLLECTION_NAME]