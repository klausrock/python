"""
A class types.SimpleNamespace provides a mechanism to instantiate 
an object that can hold attributes and nothing else.
"""

from types import SimpleNamespace
sn = SimpleNamespace(x = 1, y = 2)
print('1.',sn)
sn.x=1 ; sn.y=10
print('2.',sn)
sn.z = 'foo'
del(sn.x)
print('3.',sn)
sn.y=2; sn.z='foo'
print('4.',sn)

