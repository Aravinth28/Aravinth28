list1 = [1,2,3,4,5,6,7,8,9]
print("Original List : ", list1)

# 1. Append
list1.append(10)
print("list1.append(10) \n After appending 10 :",list1)
print()

# 1.1 Insert
list1.insert(0,100)
print("list1.insert(0,100) \n After inserting 100 at index=0 :",list1)
print()

# 1.2 Copy
list2 = ['a','b','c','d']
list2 = list1.copy()
print("list2 = list1.copy() \n After Copy list2 is :", list2)
print()

# 1.3 Extend one list with another
list2 = ['a','b','c','d']
list2.extend(list1)
print("list2.extend(list1) \n After extending list2 by list1 : ",list2)
print()

# 2. Pop
list1.pop()
print("list1.pop(0) \n After popping index=0 :",list1)
print()

# 2.1 Remove
list1.remove(5)
print("list1.remove(5) \n remove(x) removes the first ocurence of x : ",list1)
print()

# 2.3 Del
del list1[3:5]
print("del list1[3:5] \n After deleting index 3 and 4 : ", list1)

# 3.1 Sort
list1.sort()
print("list1.sort() \n After sorting the list : ",list1)
print()

# 3.2 Reverse
list1.reverse()
print("list1.reverse() \n Reversed list is ",list1)

# 3.3 Index
print("index(ele=7,beg=2,end=7) \n The index of ele between beg and end : ",list1.index(7,2,7))
print()

# 3.4 min
print("min(list1) \n Minimum element of list1 is",min(list1))
print()

# 3.5 len
print("len(list1) \n Length of list1 is",len(list1))
print()

# 3.6 max
print("max(list1) \n Maximum element of list1 is",max(list1))
print()

# 3.7 count
print("list1.count(10) \n The Count of occurences in the list is ",list1.count(10))
