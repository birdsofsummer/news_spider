from bs4 import BeautifulSoup

def arr2json(d=[],d1=''):
    t=d1.split(',')
    result={}
    for (k,v) in zip(t,d):
        result[k]=v
    return result

def parse_item(i):
    title=i.title.string
    url=i.guid.text
    img=i.enclosure['url']
    pubdate=i.pubdate.text
    category=i.category.text
    description=i.description.text
    d=[title,url,img,pubdate,category,description]
    t='''title,url,img,pubdate,category,description'''
    return arr2json(d,t)

