#!/usr/bin/python

#tuple1, tuple2 = (123, 'xyz', 'minus'), (456, 'abc')

tuple1 = (123, 'xyz', 'minus')
tuple2 = (456, 'abc')

"""
print("First tuple length: ", len(tuple1), type(tuple1))
print(Second tuple length: ", len(tuple2))
"""
tuple1, tuple2 = ('123', 'xyz', 'minus', 'abc'),(456, 700, 200) # integer to integer OR string to string

print("Min value element: ", min(tuple1))
print("Max value element:", max(tuple2))

print("Min value element:", min(tuple1))
print("Max value element:", max(tuple2))