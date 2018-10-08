'''
INDEXING
 String Special Operators
                            0 1 2 3 4 # Left to Right index
                            -5-4-3-2-1# Right to Left index
Assume string variable a = 'Hello' and b = 'Python' then:
'''

a = 'Hello'
b = 'Python'

#Accessing variables in python

print("Accessing variable i.e. a:",a[1])
print("")
print("Accessing variable i.e. b:",b[-4])

#RANGE SLICING:

print("Left to Right Index i.e a",a[0:4])
print("")
print("Right to Left Index i.e b",b[1:6])

#Raw String
print(r'\n')

#Format Operator

print("My name is %s and I was born in %d" % ('jaya',1981))

#Declaring variables
var1= 'jaya'
var2= 1981
print("My name is %s and I was born in %d" % (var1,var2)) #format operator

#{} placeholders
print("My name is {} and I was born in {}".format('Guido Van Rossum',1981))  #method

#part of method , call variables
print("My name is {} and I was born in {}".format(var1,var2))

#another way, call variables inside placeholders {}
print("My name is {var3} and I was born in {var4}".format(var3='python',var4=1981))

#indexing method,first declare variables
print("My name is {0} and I was born in {1}".format(var1,var2))
print("My name is {1} and I was born in {0}".format(var1,var2))

#Concatenation

firstname = 'Guido'
lastname = 'Rossum'

fullname = firstname + " & " + lastname
print(fullname)
fullname = firstname + " " + lastname
print(fullname)
fullname = firstname[0] + " & " + lastname[0]
print(fullname)

#print 5 times first name

print(firstname*5)

#new program

str1 = "Hello World!"  #11 characters
str2 = 'This is an example of string'

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'

print(str1[0])
print(str1[-1])
print(str1[2:6])
print(str1[2:8])
print(str1[2:7])
print(str1[:5])
print(str1*3)

print(alphabets[0::2]) #zero based indexing
print(num[0::2]) #zero based indexing
print(num[0::3]) #zero based indexing
print(num[0::6]) #zero based indexing

print("updated string ", str1[:6] + "planet")
print("updated string ", str1[:12] + "perl")

#formatting of strings

print("Your name is %s and your account id is %d" %("Kevin",14456))

print("Calling str1 {0} and calling str2 {1}".format(str1,str2))

print("Value1{} Value2{} and Value3{}".format("python",100,"pycharm"))

print("Value1 {1} Value2 {0} and Value3 {2}".format("python",100,"pycharm"))
