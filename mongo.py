import pymongo
import pprint

from bson.json_util import dumps,loads,RELAXED_JSON_OPTIONS
from bson import Binary, Code

from pymongo import MongoClient
from bson.objectid import ObjectId
import config


def head(d={}):
    if len(d) == 0 : return {}
    x,y=[(k,v) for k,v in d.items()][0]
    return {x:y}

def to_json(f):
    def wrapper(*args, **kwargs):
        r=f(*args, **kwargs)
        return dumps(r)
    return wrapper

def conn():
    u=config.CONFIG['db_url']
    DB=config.CONFIG['db']
    client = MongoClient(u)
    db=client[DB]
    return db

def col_gen():
     db=conn()
     c=config.CONFIG['table']
     col=db[c]
     return col

def init_db():
    col=col_gen()
    col.create_index([('title', pymongo.ASCENDING)], unique=False)

def list_db():
     db=conn()
     return [x['name'] for x in db.list_collections()]

def list():
    col=col_gen()
    return [x for x in col.find()]

def insert(d='{"title":"cc","content":""}'):
    col=col_gen()
    d1=loads(d)
    r=col.insert_one(d1)
    return {"_id":r.inserted_id}


def insert_many(d='[]'):
    d1=loads(d)
    col=col_gen()
    if len(d1) == 0 : return []
    r=col.insert_many(d1)
    return r.inserted_ids

def find_by_key(k="title",v=[]):
    col=col_gen()
    return col.find( { k: { "$in": v} } )

def find(s="{}"):
    col=col_gen()
    s1=loads(s)
    return col.find_one(s1)

def find_by_id(i=""):
    col=col_gen()
    return [x for x in col.find({"_id": ObjectId(i)})]

def update_by_id(d="{}"):
    col=col_gen()
    d1=loads(d)
    if len(d1) == 0 : return {}
    s={"_id":d1['_id']} if d1.get('_id') else head(d1)
    return col.find_one_and_update(s,{"$set":d1})

def update_by_id1(i="",d="{}"):
    col=col_gen()
    d1=loads(d)
    return col.update({"_id":ObjectId(i)},d1)

def update(s="{}",d="{}"):
    col=col_gen()
    s1=loads(s)
    d1=loads(d)
    return col.update(s1,d1)
def update_one(s="{}",d="{}"):
    col=col_gen()
    s1=loads(s)
    d1=loads(d)
    return col.update_one(s1,d1)
def update_many(s="{}",d="{}"):
    col=col_gen()
    s1=loads(s)
    d1=loads(d)
    return col.update_many(s1,d1)
def delete_one(s="{}"):
    col=col_gen()
    s1=loads(s)
    r=col.delete_one(s1)
    return r.raw_result
def delete_by_id(i=""):
    col=col_gen()
    r=col.delete_one({"_id":ObjectId(i)})
    return r.raw_result
def delete_many(s="{}"):
    s1=loads(s)
    col=col_gen()
    r=col.delete_many(s1)
    return r.raw_result
def count():
    col=col_gen()
    r=col.count_documents({})
    return r

