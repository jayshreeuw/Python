#!/usr/bin/python

dict ={"firstname":'Guido', "middlename":'Van', "lastname":'Rossum', 'Age':58}

print(dict)

print("End Len : %d" % len(dict))

print(dict,type(dict),id(dict))

dict_5 = dict.copy() #copy() is a method

dict.clear()
print("Calling a Dict Variable:" ,dict)

print("New Dictionary: %s" % str(dict_5))