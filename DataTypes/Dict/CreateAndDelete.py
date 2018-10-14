#!/usr/bin/python

guido = {'name':'van', 'age':60, 'class':'first'}

print(guido,type(guido), id(guido), len(guido), dict(enumerate(guido)))

print("guido['name']:", guido['name'])  #calling keys

print("guido['age']:", guido['age']) # calling keys

print("guido['class']:", guido['class']) # calling keys

del guido['name']   # removes entry with 'name'

print(guido)

#del guido #this deletes the entire variable

#print(guido) #after deleting it will not print

guido.clear()   #removes all entries in dict #Clear is a method
print(guido)  #prints empty dictionary