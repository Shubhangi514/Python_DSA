#-Playing with Arrays-#
#-creating an array and traversing it-#
from array import *
my_array = array('i',[1,2,3,4,5,6,7,8,9,10])
#-traversing-#
for i in my_array :
    print(i)
#-access individual element through indexes-#
print(my_array[9])
#-append any value  using append() function-#
my_array.append(0)
print(my_array)
#-insert value in an array using insert() method-#
my_array.insert(5, 0)
print(my_array)
#-extend python array using extend() method-#
my_array1 = array('i', [11,12,13,14,15])
my_array.extend(my_array1)
print(my_array)
#-add items from list into array using fromlist() method-#
mylist = [16,17,18,19,20]
my_array.fromlist(mylist)
print(my_array)
#-Remove any array elemnt using remove method-#
my_array.remove(17)
print(my_array)
#-remove last array element using pop() method-#
my_array.pop(7)
print(my_array)
#-fetch any element through its index using index() method-#
print(my_array.index(19))
#-reverse a python array using reverse() method-#
my_array.reverse()
print(my_array)
#-get array buffer information through buffer_info() method-#
print(my_array.buffer_info())#iska output array ka start address btata hai or har bar run krne par new address deta hai 
#-check for number of occurance of an element using count() method-#
print(my_array.count(0))
#-convert array to string using tostring() method-#
strTemp = my_array.tostring()
print(my_array.tolist())
ints = array('i')
ints.fromstrinf(strTemp)
print(ints)
