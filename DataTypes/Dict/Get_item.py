#!/usr/bin/python

student = {'name': 'jay', 'age': 35} # Dictionary variable

print("Value:", student.get('age'))

print("Value:", student.get(7)) # we cannot call a value

print("Value: %s" % student.get('Age'))

print("Value: %s" % student.get('Education','Python')) #this will print python in the output
#because the key-education does not exist in the variable-student

filename = {'course':'python', 'mode':'video', 'boolean':1}
sample = {1:"one", 2:"two"}
print(filename.get('mode'))
print(filename.keys())
print(filename.values())
print(filename.items())

dict_1 = {'name':"jaya", 'age':34}
print("value: %s" % dict_1.keys())
print("value: %s" % dict_1.values())