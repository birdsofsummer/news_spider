import re,sys, time, os, json, random
[sys.path.append(sys.path[0]+x) for x in ["/vendor"]]

import numpy
import rx
from rx import operators as ops
from .parser.test  import *

def test_numpy():
    print(dir(numpy))
def test_rxpy():
    source = rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")
    composed = source.pipe(
        ops.map(lambda s: len(s)),
        ops.filter(lambda i: i >= 5)
    )
    composed.subscribe(lambda value: print("Received {0}".format(value)))
test_rxpy()
