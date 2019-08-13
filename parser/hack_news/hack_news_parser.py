import json
import sys
from bs4 import BeautifulSoup

def text(x):
    return x.text.replace('\n','').strip() if not x is None else ""

def num(x):
    c=text(x)
    d=eval(c) if len(c)>0 else 0
    return d

def arr2json(d=[],d1=''):
    t=d1.split(',')
    result={}
    for (k,v) in zip(t,d):
        result[k]=v
    return result

def parse_article(x):
    t=x.find('h3').find('a')
    title,url=t.string,t['href']
    score=num(x.find(title="Score"))
    cm=x.find(rel="comment")
    comment_url=cm['href'] if not cm is None else ""
    comment_acc=num(cm)
    host_i=x.find(title="Host").find('img')
    host_icon=host_i['src'] if not host_i is None else ""
    host=text(x.find(title="Host").find('span'))
    submitted_time=x.find(title="Submit time").find('span')['data-submitted']
    au=x.find(title="Author")
    author_u=au.find('a')['href'] if not au is None else ""
    author=text(au.find('span')) if not au is None else ""
    img=x.find('img',lazyload="on")
    img_url='http://hackernews.betacat.io'+ img['data-original'] if not img is None else ""
    c=x.select('div[class="summary-text"]')
    content=text(c[0]) if len(c)>0 else ""
    d=[title,url,content,score,img_url,comment_url,comment_acc,author_u,author,img_url,submitted_time,host, host_icon]
    d1='''title,url,content,score,img_url,comment_url,comment_acc,author_u,author,img_url,submitted_time,host,host_icon'''
    return arr2json(d,d1)

def hack_news_parser(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [parse_article(x) for x in soup.find_all('article')]
