# -*- coding: utf-8 -*-

from ajax import *
from api  import *

def weibo_history(n=1):
    day=last_days(n)
    types=["realTimeHotSearchList","douyin","toutiao","douban"]
    search_params=[ {"type" : t ,"date" : d } for t in types for d in day]
    url=api['weibo']['url']
    return gets(url,search_params)

def reso(params={"type":"realTimeHotSearchList"}):
    url=api['weibo']['url']
    return get(url,params)

def word_cloud(t=0):
    dayTypes=["now","today","yesterday",]
    dayType=dayTypes[t] or "today"
    params= {"dayType":dayType}
    url=api["word_cloud"]['url']
    return get(url,params)

def word_clouds():
    return [word_cloud(x) for x in  range(3)]

def search(keyword):
    url=api["search"]['url']
    params=extend(api['search']['params'],{"keyword":keyword})
    return get(url,params)



