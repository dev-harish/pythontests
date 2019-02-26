import weakref
import gc

class MyObject(object):
    def my_method(self):
        print ('my_method was called!')

obj = MyObject()
r = obj
print(r)
gc.collect()
print(r)
assert r is obj,"dsdsd"

obj = 1   #Let's change what obj references to
gc.collect()
assert r is None ,"deleted"
print(r)