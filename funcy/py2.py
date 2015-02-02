import sys

from .calc import *
from .colls import *
from .decorators import *
from .funcolls import *
from .funcs import *
from .seqs import *
from .types import *
from .strings import *
from .flow import *
from .objects import *
from .namespaces import namespace
from .debug import *
from .primitives import *


# Setup __all__
modules = ('calc', 'colls', 'decorators', 'funcolls', 'funcs', 'seqs', 'types',
           'strings', 'flow', 'objects', 'namespaces', 'debug', 'primitives')
__all__ = cat(sys.modules['funcy.' + m].__all__ for m in modules) + ['flip']


from collections import Mapping

def flip(value):
    def flip_pair(pair):
        k, v = pair
        return v, k

    if isinstance(value, Mapping):
        return walk(flip_pair, value)
    else:
        return lambda x, y: value(y, x)


# Python 2 style zip() for Python 3
from .cross import PY3
if PY3:
    _zip = zip
    def zip(*seqs):
        return list(_zip(*seqs))
    __all__.append('zip')
else:
    zip = zip
