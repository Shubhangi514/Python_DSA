# myList = [10,20,30,40,50,60,70,80,90]
# if 10 in myList:
#     print(myList.index(70))
# else:
#     print('the value does not exist in the list')
# list funtions and operations
a = [1,2,3,4]
b = [5,6,7,8]
c = a * 2 + b * 3
print(len(c))
print(max(b))
print(min(c))
print(sum(c)/len(c))
#question
# total = 0
# count = 0
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#     avg = total / count
# print('Average: ', avg)

# now you have to make a list out of the following code above

# mylist = list()
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     mylist.append(value)
#     # avg = total / count
# print(sum(mylist)/len(mylist))

# strings and list

a = 'Hey i am Learning new things about lists'
b = list(a)
c = a.split()
print(b)
print(c)
# now if we have a string like this 
d = 'hello/my/name/is/shubhi'
delimiter = '/'
e = d.split(delimiter)
# here delimiter works as avoider where wee want to avoid anything within the string
print(e)
print(delimiter.join(a))
#drawbacks of list
# 1. most list arguments modify the argument and return null
mylist = [2,5,6,3,8,19,57,39,80]
sorted(mylist)
# mylist = mylist.sort()
print(mylist)
# 2. since wee have alot of method to add or delete element on a list we might get confused by the syntax
# 3. if we used or manipulate the original list we might loose the original list therfore we should always make a copy of original list 
# sorted()-this function returns a new sorted list from the items in iterables  

# LISTS Vs ARRAYS
import numpy as np
# SIMILARITIES: both are mutable , both can be indexed ans iterated , both can be sliced.....
myArray = np.array([1,2,3,4,5,6,7,8,9])
_list = [1,2,3,4,5]
print(myArray/2)  #arithmetic operations can only be performed in arrays
# data types can be diff. in lista but can't be in array
