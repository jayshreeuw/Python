#!/usr/bin/python

#DICTIONARY IS A MUTABLE DATA TYPE

dict1 ={'name':'minu', 'Age': 7, 'class': 'first'}

print(dict1)

dict1['Age'] = 8 #update existing entry

print(dict1)

dict1['School'] = "DPS" # Adds a new entry

print(dict1, dict(enumerate(dict1)))

print("dict['Age']:", dict1['Age'])

print("dict['School']:", dict1['School'])

print(dict1,dict(enumerate(dict1)))

print(dict1)
