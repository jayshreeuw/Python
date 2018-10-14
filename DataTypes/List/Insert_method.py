#

aCool_List = ["superman", "spiderman", 1947, 1987, "Spiderman"]

oneMoreList = [22,34,56,34,34,78,98]

print(list(enumerate(aCool_List)))

# Inserting values

aCool_List.insert(0,"street750")
print(aCool_List)

print(list(enumerate(aCool_List)))

oneMoreList.insert(5,1947)
print(oneMoreList)
print(list(enumerate(oneMoreList)))

'''
list.insert(i,x):
Insert an item at a given position.
First argument is the index of the element before which to insert,
so a.insert(0,x) inserts at the front of list and a.insert(len(a),x)
is equivalent to a.append(x)
'''