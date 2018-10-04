#!/usr/bin/python

#! = shebang
# /usr/bin/python = Absolute path of where python is installed

# Comments in Python

#Single line comments are: 1.#, 2.'', 3."", 4. ''' ''' & 5. """ """

#Multi line comments are: 1. ''' ''' & 2.""" """

#Creating variables in Python

''' Rule of creating variables in Python
1. A-Z
2. a-z
3. 0-9 :Integer value should not be created as prefix of any variable _lname
4. A_Za-z
5. A-Zz-z0-9
6. _
7. A_Za-z0-9_
'''

# Creating String variables:

FNAME = 'Guido'         #Single Quotes
mname = "Van"           #Double Quotes
_lname = """rossum"""   #Double Triple Quotes
software_001 = '''Python 3.6.0'''   #Single triple quotes

#Accessing variables with the help of print()

print(FNAME)
print("")
print(mname)
print("")
print(_lname)
print("")
print(software_001)

# Verify the variable Data Type using type():

print(type(FNAME))
print("")
print(type(mname))
print("")
print(type(_lname))
print("")
print(type(software_001))