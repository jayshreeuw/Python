#!/usr/bin/python
'''
var = 10

if var == 20:
    print("1- Got a true expression value")
    print(var)
elif var == 11:
    print("2- Got a true expression value")
    print(var)
elif var == 12:
    print("3- Got a true expression value")
    print(var)
elif var == 13:
    print("4- Got a true expression value")
    print(var)
elif var == 17:
    print("5- Got a true expression value")
else:
    print("Else block 4 - Got a false expression value")
    print(var)

print("Good Bye!")
'''

number = 23
guess = int(input("Enter an integer: "))

if guess == number:
    #New block starts here
    print('Congratulations, you guessed it.')
    print('but you do not win any prizes!')
    #New block ends here
elif guess < number:
    #Another block
    print('No, it is little higher than that')
    #You can do whatever you want in a block ...
else:
    print('No, it is little lower than that')
    #You have guessed > number to reach here

print("Done")

#This last statement is always executed
#After the IF statement is executed