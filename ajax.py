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

def http(url):
    s = requests.Session()
    s.headers.update(headers_gen(url))
    return s

def get(url,params={}):
    s=http(url)
    return s.get(url,params=params).json()

def get1(u,p={}):
    headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }
    r=requests.get(u,params=p,headers=headers)
    r.encoding='utf-8'
    return r.text


def gets(url,params=[]):
    return [get(url,x) for x in params]


def last_days(n=365):
    now=datetime.datetime.now()
    return [(now-datetime.timedelta(days=x)).strftime('%Y/%m/%d') for x in range(n)]

