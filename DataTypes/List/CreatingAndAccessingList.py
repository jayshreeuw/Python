# List is a mutable sequence of values
#syntax:
#a_list[index] = value

numbers = [4,8,19,23]

print('To check index value of each element in a variable:',list(enumerate(numbers)))
print('Accessing a list variable:',numbers)

print(numbers)

numbers[1] = 27
print(numbers)
print("Append or modify a existing element value:", numbers)

numbers[0] = 17
print(numbers)

numbers[3] = 53
print(numbers)

