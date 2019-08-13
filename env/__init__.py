import os
import sys
print(__name__)
print(__file__)
print(__path__)

def init_env():
    r=os.path.split(os.path.realpath(__file__))
    r1='/'.join(r[0].split('/')[:-1])
    sys.path.append(r1)
    r2=os.getcwd()
    print(r1)
    print(r2)
    [sys.path.append(r1+"/"+x) for x in ["vendor"]]
    print(sys.path)


init_env()
