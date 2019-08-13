# -*- coding: utf-8 -*-

import sys
import logging
import datetime
import time
import requests
import json
import functools

def extend(a,b):
    return dict(a,**b)

def headers_gen(url):
    headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "referrer": url,
    }
    return headers


cors_headers={
    'access-control-allow-origin': '*',
    'access-control-allow-methods': 'GET,POST,PUT,PATCH,TRACE,DELETE,HEAD,OPTIONS',
    'access-control-allow-headers': 'accept,accept-encoding,cf-connecting-ip,cf-ipcountry,cf-ray,cf-visitor,connection,content-length,content-type,host,user-agent,x-forwarded-proto,x-real-ip,accept-charset,accept-language,accept-datetime,authorization,cache-control,date,if-match,if-modified-since,if-none-match,if-range,if-unmodified-since,max-forwards,pragma,range,te,upgrade,upgrade-insecure-requests,x-requested-with,chrome-proxy,purpose,accept,accept-language,content-language,content-type,dpr,downlink,save-data,viewport-width,width',
    'access-control-max-age': '1728000',
}

def res_json(d={}):
    h= {"Content-Type":"application/json; charset=utf-8"}
    h1=extend(h,cors_headers)
    r={"errorCode":0,"errorMessage":"","ok":True,"data":d}
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers":h1,
        "body": json.dumps(r),
    }

def json_dec(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(*args)
        print(**kwargs)
        r=f(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" % execution_time)
        return res_json(r)
    return wrapper

def deco01(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        r=f(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" % execution_time)
        return r
    return wrapper

@json_dec
def echo(a,b):
    return (a,b)

def echo_handler():
    return {
                "POST":echo,
                "GET":echo,
                "PUT":echo,
                "DELETE":echo,
           }

class App:
    def __init__(self):
        self.router={
            "/" :echo_handler(),
            "/echo":echo_handler(),
        }
    def route(self,path="/",methods=["GET","POST"]):
        def f1(f):
            if path not in self.router :
                self.router[path]={}
            for x in methods:
                self.router[path][x]=f
            @functools.wraps(f)
            def f2(*args, **kwargs):
                return f(*args, **kwargs)
            return f2
        return f1
    def run(self,event,content):
        prefix= event["requestContext"]["path"]
        path=event["path"]
        p1= path.replace(prefix,'').strip()
        r=self.router
        httpMethod=event["httpMethod"]
        if (p1 in r) and (httpMethod in r[p1]):
            f=r[p1][httpMethod]
            return f(event,content)
        else:
            f=echo
            return f(event,content)

def test_main():
    app=App()
    @app.route(path="/ccc",methods=["GET","POST"])
    @json_dec
    def main_handler(event,content={}):
            body=event["body"]
            headerParameters=event["headerParameters"]
            queryString=event["queryString"]
            queryStringParameters=event['queryStringParameters']
            sourceIp=event['requestContext']["sourceIp"]
            print(body)
            return event
  #  logger.info('start main_handler')
  #  logging.basicConfig(level=logging.INFO, stream=sys.stdout)
  #  logger = logging.getLogger()
  #  logger.setLevel(level=logging.INFO)
  #  logger.info('Loading function')
    d={'body': '{"x":1,"y":2}', 'headerParameters': {}, 'headers': {'accept': '*/*', 'content-length': '7', 'content-type': 'application/x-www-form-urlencoded', 'endpoint-timeout': '15', 'host': 'service-75ph8ybo-1252957949.ap-hongkong.apigateway.myqcloud.com', 'user-agent': 'curl/7.61.1', 'x-anonymous-consumer': 'true', 'x-qualifier': '$LATEST'}, 'httpMethod': 'POST', 'path': '/weibo/ccc', 'pathParameters': {}, 'queryString': {}, 'queryStringParameters': {}, 'requestContext': {'httpMethod': 'ANY', 'identity': {}, 'path': '/weibo', 'serviceId': 'service-75ph8ybo', 'sourceIp': '58.60.1.25', 'stage': 'release'}}
    z=app.run(d,{})
    print(z)
    return z

