#!/usr/bin/python

aCool_List = ["superman", "spiderman", 1947, 1987, "Spiderman"]

oneMoreList = [22,34,56,34,34,78,98]

#deleting values

aCool_List.pop(1)

print(aCool_List)

#Without index using pop method:
aCool_List.pop()
print(aCool_List)

'''
list.pop([i]):list.pop()
Remove the item at the given position in the list and return it;
If no index is specified, a.pop() removes and return the last item in the list
'''