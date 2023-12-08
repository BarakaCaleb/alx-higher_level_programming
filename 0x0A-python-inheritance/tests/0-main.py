#!/usr/bin/python3

lookup = __import__('0-lookup').lookup


class Myclass1(object):
    pass

class Myclass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
