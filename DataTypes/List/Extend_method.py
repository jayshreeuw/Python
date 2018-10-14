#!usr/bin/python

aCool_List = ["superman", "spiderman", 1947, 1987, "Spiderman"]

oneMoreList = [22,34,56,34,34,78,98]

#extending the list

#Before:

print(aCool_List)
print(type(aCool_List), len(aCool_List), id(aCool_List), list(enumerate(aCool_List)))

print(oneMoreList)
print(type(oneMoreList), len(oneMoreList), id(oneMoreList), list(enumerate(oneMoreList)))

aCool_List.extend(oneMoreList)

#After:

print(aCool_List)
print(type(aCool_List), len(aCool_List), id(aCool_List))

'''
Extend the list by appending all the items in the given list;
equivalent to a[len(a):] = L
'''
