from so import *
from app import *
import json
from spider import hack_news
import spider as s
import env

def main(event,content):
    app=App()

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
    def hack_news_handler(event,content={}):
        queryString=event["queryString"]
        n=queryString.get("n") or 3
        n1=int(n)
        return s.reutersmedia(n1)

    @app.route(path="/huanqiu",methods=["GET","POST"])
    @json_dec
    def hack_news_handler(event,content={}):
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

