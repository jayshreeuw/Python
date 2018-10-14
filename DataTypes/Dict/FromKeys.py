#!/usr/bin/python

seq = ('name', 'age', 'gender') # a tuple variable

dict1 = dict.fromkeys(seq) # calling a tuple variable as part of dict.fromkeys method

print("new dictionary: %s", str(dict1))

dict2 = dict.fromkeys(seq,10) # assigning values to keys

print("new dictionary: %s" % str(dict2))