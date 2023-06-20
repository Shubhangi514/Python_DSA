# Searching Algorithms: this means like we created a login page and two users tryied to log in and first entered a name and second is trying to create an account of the same name so this algorithm we can give the user 2 an output message as the user name is already taken this how this works
# Now searching algorithm is basically of two types :- (1) Linear Search (2) Binary Search
# LINEAR SEARCH: In this technique the items are searched one by one and are applicable in sorted and unsorted arrays, it is also know as SEQUENTIAL SEARCH ,Time Complexity - O(N) & Space Complexity - O(1) , linear search is good in case of unsorted arrays but in case of sorted arrays we can use other algorithms to increase the efficiency

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return "Value Found!!"
    return "Value Not Found !"

# BINARY SEARCH: This technique is much more faster than linear serch (2) half of the remaining element can be eliminated at a time ,instead of eliminating them one by one (3) works only with sorted arrays 

import math
def binarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    while not(array[middle]==value) and start<=end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1 
        middle = math.floor((start+end)/2)
        # print(start, middle, end)  
    if array[middle] == value:
        return middle
    else:
        return -1

print(linearSearch([20,40,30,50,90], 90))

print("-------------")

custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))