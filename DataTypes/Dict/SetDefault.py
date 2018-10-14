#!/usr/bin/python

var1 = {'name': 'john', 'age': 22}

print("value: %s" % var1.setdefault('age', None))

print("value: %s" % var1.setdefault('course', None))

