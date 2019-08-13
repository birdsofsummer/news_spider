import os
import sys

print(__name__)
print(__file__)
print(__path__)

def pwd():
    r=os.path.split(os.path.realpath(__file__))
    return r[0]

def walk(x):
    return [b for (a,b,c) in os.walk(x)][0]

def init_env():
    p=pwd() if len(sys.path[0]) == 0 else sys.path[0]
    sys.path.append(p)
    [sys.path.append(p+"/"+x) for x in walk(p)]
    print(sys.path)

init_env()
