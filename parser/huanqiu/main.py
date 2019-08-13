from bs4 import BeautifulSoup
import json

def tuple2json(d=[]):
    j={}
    for (a,b) in d:
        j[a]=b
    return j

def parse_item1(i):
    return [(x.name.strip(),x.string.strip() if x.string else "" ) for x in i.children if not x.name is None]

def parse(cc=""):
    if len(cc) == 0 : return []
    y=BeautifulSoup(cc,features="html.parser")
    c=y.rss.channel
    d1=[(x.name,x.text) for x in c.children if not x.name is None and  x.name != "item"]
    j1=tuple2json(d1)
    print(j1)
    d2=[parse_item1(x) for x in c.findAll('item')]
    d3=[tuple2json(x) for x in d2]
    r={ "info":j1, "item":d3, }
    return r

def save(dd=[],name='./index.json'):
    z=json.dumps(dd)
    with open(name,'w') as f:
        f.write(z)

def test():
    with open('./topnews.xml') as f:
        cc=f.read()
        d=parse(cc)
        save(d)
        print(d)
