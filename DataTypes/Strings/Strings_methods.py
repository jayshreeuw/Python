#!usr/bin/python

# 1. Capitalize() method:
#It returns a copy of the string with only its first character capitalized

str = "this is string example....wow!!!"
print("str.capitalize():",str.capitalize())

# 2. Center()  method:
# This method returns centered  in a string of length width.
#Padding is done using a specified fillchar, default filler is a space.

str1 = "Welcome to python world"
print(len(str1)) # len() prints the number of characters in  string
print("str.center(27,'a'):",str1.center(27, '$'))

# 23 is the length of the character and 4 we have added
# two $ signs are added in suffix and two in prefix

# 3. Count() method:
# It returns the number of occurences of substring sub in the range [start,end]
# Optional arguments start and end are interpreted as in slice notation

mac = "Welcome to python world"
sub = "o"
print(len(mac))
print("mac.count(sub):", mac.count(sub))
print("mac.count(sub,4,23:", mac.count(sub, 4, 23))
sub1='python'
print("mac.count(sub1,4,23:", mac.count(sub1, 4, 23))

# 4. Decode() method:
#It defaults to the default string encoding

mac1 = "Welcome to python"
mac1 = mac1.encode('utf-8','strict')
print("Encoded String: ", mac1)
print("Decoded String: " + mac1.decode('utf-8','strict'))

#5. Encode() method:
#It returns an encoded version of the string


#6. Endswith() method:
#It returns TRUE if the string ends with the specified suffix otherwise returns FALSE

str2 = "this is string example....wow!!!";

suffix = "wow!!!";
print(str2.endswith(suffix))
print(str2.endswith(suffix,20))

suffix = "is";
print(str2.endswith(suffix, 2, 4))
print(str2.endswith(suffix, 2, 6))