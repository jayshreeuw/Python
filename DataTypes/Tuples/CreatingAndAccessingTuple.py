#!/usr/bin/python

tup1 = ('python', 'linux', 1997, 2000)
tup2 = (1,2,3,4,5)
tup3 = "A", "B", "C", "D", "E"
tup4 = 'a', 'b', 'c', 'd'

# Tuple can be created with either open-close parentheses or quotes
# Once a tuple is created it cannot be modified, tuple is immutable data type

print(tup1, type(tup1), id(tup1), len(tup1))
print("") #adds new line
print(tup2, type(tup2), id(tup2), len(tup2))
print("")
print(tup3, type(tup3), id(tup3), len(tup3))
print("")
print(tup4, type(tup4), id(tup4), len(tup4))

#Call the tuple using index:
print(tup3[1])

print(tuple(enumerate(tup1)))
