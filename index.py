import json
from so import *
from app import *
import spider as s
import upload_auth
import env
import time
import mongo

def now():
    t = "{}".format(time.time()).replace('.','')
    return t

def main(event,content):
    app=App()

    @app.route(path="/doc",methods=["GET"])
    @bson_dec
    def list_doc(event,content):
        queryString=event["queryString"]
        i=queryString.get("id")
        if i is None :
            return mongo.list()
        else:
            return mongo.find_by_id(i)

    @app.route(path="/doc",methods=["PUT"])
    @bson_dec
    def update_doc(event,content):
        body=event.get('body')
        return mongo.update_by_id(body)

    @app.route(path="/doc",methods=["DELETE"])
    @bson_dec
    def del_doc(event,content):
        queryString=event["queryString"]
        i=queryString.get("id")
        if i is None  or i is None: return {}
        return mongo.delete_by_id(i)

    @app.route(path="/doc",methods=["POST"])
    @bson_dec
    def add_doc(event,content):
        body=event.get('body')
        if body is None : return {}
        return mongo.insert(body)

    @app.route(path="/docs",methods=["POST"])
    @bson_dec
    def add_docs(event,content):
        body=event.get('body')
        if body is None : return {}
        return mongo.insert_many(body)


    @app.route(path="/echo1",methods=["GET","POST","PUT","DELETE"])
    @json_dec
    def echo1(event,content):
        return event

    @app.route(path="/upload_tk",methods=["GET","POST"])
    @json_dec
    def upload_tk(event,content={}):
        return upload_auth.main()

    @app.route(path="/upload",methods=["GET","POST"])
    @json_dec
    def upload(event,content={}):
        body=event["body"] if "body" in event else ""
        headerParameters=event["headerParameters"]
        queryString=event["queryString"]
        queryStringParameters=event['queryStringParameters']
        sourceIp=event['requestContext']["sourceIp"]
        n=queryString['name'] if 'name' in queryString else ""
        file_name="/test/"+now()+n
        import upload
        return upload.upload_stream(file_name,body)

    @app.route(path="/sputni",methods=["GET","POST"])
    @json_dec
    def sputnik(event,content={}):
        return s.sputniknews()

    @app.route(path="/hack_news",methods=["GET","POST"])
    @json_dec
    def hack_news_handler(event,content={}):
        return s.hack_news()

    @app.route(path="/vbc",methods=["GET","POST"])
    @json_dec
    def vbc_handler(event,content={}):
        queryString=event["queryString"]
        n=queryString.get("n") or 3
        n1=int(n)
        return s.reutersmedia(n1)

    @app.route(path="/huanqiu",methods=["GET","POST"])
    @json_dec
    def huanqiu_handler(event,content={}):
        queryString=event["queryString"]
        n=queryString.get("n") or 12
        n1=int(n)
        return s.huanqiu(n1)

    @app.route(path="/news",methods=["GET","POST"])
    @json_dec
    def news_handler(event,content={}):
        return s.news()


    @app.route(path="/ccc",methods=["GET","POST"])
    @json_dec
    def main_handler(event,content={}):
            body=event["body"] if "body" in event else ""
            headerParameters=event["headerParameters"]
            queryString=event["queryString"]
            queryStringParameters=event['queryStringParameters']
            sourceIp=event['requestContext']["sourceIp"]
            print(body)
            return event
    return app.run(event,content)

