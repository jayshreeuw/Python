#!/usr/bin/python

tup = ('python', 'linux', 1997, 2000)

print(tup)

del tup
#del tup[0], #type error: tuple object does not support item deletion

print("After  deleting tup:")

print(tup) #name error: name 'tup' is not defined

#cannot delete specific index