# Syntax: lambda [arg1 [,arg2,.....argn]]:expression

#!/usr/bin/python

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))