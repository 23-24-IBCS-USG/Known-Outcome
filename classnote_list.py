myList = [45, 20, 10, "yellow", True]

print(myList)

#these loops do the same thing 
for item in myList:
    print(item)

for i in range(len(myList)):
    print(myList[i])

# add items to a list

myList.append("abby")
print(myList)

#will be inserted at position 2
myList.insert(2,"vera")
print(myList)

#remove items from a list
myList.pop()
print(myList)

#remove at particular index
myList.pop(2)
print(myList)

#remove specific elements
myList.remove("yellow")
print(myList)


#check to see if an item is in the list
if 45 in myList:
    print(True)
else:
    print(False)


