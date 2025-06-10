l = [1,2,3,"sai","gbaar",2]
print("actual list :-",l)

# use remove() it required to give values which we want to remove but it only remove fist occurence of element
l.remove(2)
print("use remove method to remove value :- ",l)

l.remove(l[1])
print("remove method with index to remove value ",l)

l.remove(9)
print("out of range value :-",l)

l.remove(l[1],2)
print("use both index and value",l)

#use pop() it required to give index if index is  not given bydefault it take(-1) and remove last index value
l.pop(2)
print("list which pop given index value :- ",l)

l.pop()
print("list where pop index is not given last index value :-",l)

l.pop(l[1],2)
print(l)


# Use remove(value) when you only care about deleting a particular value.
# Use pop(index) when you need the deleted item (for processing, storing) or are manipulating the list by index.
# Prefer pop() for stack-like behavior.
