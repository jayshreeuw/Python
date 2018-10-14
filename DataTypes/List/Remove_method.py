#!/usr/bin/python

aCool_List = ["superman", "spiderman", 1947, 1987, "Spiderman"]

oneMoreList = [22,34,56,34,34,78,98]

print(aCool_List)

aCool_List.remove('Spiderman')
print(aCool_List)

aCool_List.remove(2017) #2017 is not in the list
print(aCool_List)

#deleting values
aCool_List.pop(1) #with specific index
print(aCool_List)

aCool_List.pop() #last element from the list
print(aCool_List)


'''
list.remove(x):
Remove the first item from the list whose value is x.
It is an error if there is no such item
'''