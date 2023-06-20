import math
# what is sorting ? refers to arranging data in a perticular format : either ascending or descending
# types of sorting : (1) space used [(a) in place: sorting algorithm which does not require any extra space for sorting. eg:- bubble sort (b) out place: sorting algorithm which requires an extra space for sorting . eg:- merge sort] (2) stability [(a)stable: if a sorting algorithm after sorting the content does not change the sequence of similar content in which they appear then this sorting is called stable sorting . eg:- insertion sort (b) unstable: if a sorting algorithm after sorting the content changes the sequence of a similar content in which they appear , then it is called unstable sort. eg:- quick sort]
# Sorting Terminology : (1) Increasing order: as the name suggests starts from smaller terms and moves to larger terms (2) Decreasing order: visa versa of increasing order (3) Non-Increasing order: here the flow is in decreasing order terms but with a twist that is equal numbers are kept after another (4) Non-Decreasing order: visa versa of non increasing order


# BUBBLE SORT : (1)this is also called sinking sort(2)we repeatedly compare each pair of adjacent item and swap them if they are in the wrong order

def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)

# TC - O(N^2) & SC - O(1)

# SELECTION SORT: (1) in case of selection sort we repeatedly find the minimum element and move it to the sorted part of array to make unsorted part sorted. (2) main advantage of selectiion sort is that it performs well in small list (3) primary disadvantage is  its poor performance with large lists (4) its performance is easily influenced by the  by the initial ordering of items before sorting the items

def  selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i + 1, len(customList)):
            if  customList[min_index] < customList[j]:
                min_index = j
        customList[i],customList[min_index] = customList[min_index], customList[i]
    print(customList)

# TC - O(N^2) & SC - O(1)

# INSERTION SORT: (1)divide the given array in two parts (2) take first element from unsorted array and find its correct position in sorted array (3) repeat until unsorted array is empty

def insertionSort(customList):
    for i in range(1, len(customList)):
        key =  customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1  #this statement is imp coz without this the sorting will run infinitly
        customList[j+1] = key
    # print(customList)
    return customList

# TC - O(N^2) & SC - O(1)

# when to use insertion sort? (1) when we have insuffcient memory(2)easy to implement(3)when we have continous inflow of number and we want to keep them sorted
# when to avoid? when time is a concern

# BUCKET SORT: (1) create bucket and distribute elements of array into bukets (2) sort buckets individially (3) merge buckes after sorting 
# now in case of how wil we create a bucket and what will be the number of buckets ? no of buckets = round(sqrt(number of elements)) 
# to check which element will go in which bucket ? appropriate bucket = cell(value*no.of buckets/max value) then we have to sort them within buckets

def bucketSort(customList):
    numberofBucket = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBucket):
        arr.append([])

    for j in customList:
        index_b = int(j*(numberofBucket)/(maxValue+1))
        arr[index_b].append(j)

    # Check if the last element needs a separate bucket
    if len(arr[-1]) != len(customList) // numberofBucket:
        # we check if the last bucket (arr[-1]) has a different number of elements than the desired distribution (len(customList) // numberofBucket). If the last bucket has a different number of elements, it means that the last element needs to be placed in a separate bucket.  
        numberofBucket += 1
        arr.append([])
        extra_value = arr[-2].pop()
        arr[-1].append(extra_value)
        # In that case, we increment the number of buckets (numberofBucket += 1), create an extra bucket using arr.append([]), and move the last value from the second-to-last bucket to the extra bucket using extra_value = arr[-2].pop() and arr[-1].append(extra_value).

    for i in range(numberofBucket):
        # arr[i] = insertionSort(arr[i]) #we should always use quick sort in this case
        arr[i] = sorted(arr[i])

    k = 0
    for i in range(numberofBucket):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

# TC - O(N^2) & SC - O(N)
# when  to use bucket sort ? when input uniformly distributed over range [numbers ke bich me bahut bada gap nhi hona chahiye]
# when to avoid? when space is a concern

# MERGER SORT: (1) is a divide and conquer algorithm (2) divide the input array in two halves and we keep halving recursively until they become too small that cannot be broken further (3) merge halves by sorting them. 

def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m 

    L = [0] * (n1) # here division of custom list is done in two sub arrays
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l+i]
    
    for j in range(0, n2):
        R[j] = customList[m+1+j]

    i = 0 # this is the initial index of first sub array
    j = 0 # this is the initial index of second sub array
    k = l # this is the initial index of merged sub array
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1 
        k += 1
    while j < n2:
        customList[k] = R[j]
        j += 1 
        k += 1
        # now when loop starts we have combined them in sorted order

def mergeSort(customList, l, r):
    if l < r :
        m = (l+(r-1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)
        merge(customList, l, m, r)
    return customList

# TC - O(NlogN) & SC - O(N)

# QUICK SORT: (1) it is a divide and conquer algo (2) find pivot number and make sure smaller number located at the left of pivot and bigger number at the right of the pivot (3) unlike merge sort extra space is not required (4) take the right most number as pivot(5) when both left and right marker collide they are swapped with the pivot and then the pivot number is considered as fully sorted  also in this case check if the number at which they collide is smaller or grater than pivot number or not then only swap(6) after 6 being sorted we consider the lift subtree as left sequence and right subtree as right sequence and solve them separately (7) when the left marker collides the pivot number then the pivot number is considered as the largest number and only right marker is swapped 

def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low,high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i+1)

def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi-1)
        quickSort(customList, pi+1, high)

# HEAP SORT : (1) insert dta to binary heap tree (2) extract data from binary heap (3) it isbest suited with array,it does not work with linked list (4) in case of heap sort we always use minimum binary heap (5) while extracting any element from binary heap we can only extract the parent element 

def heapify(customList, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and customList[l] < customList[smallest]:
        smallest = l
    
    if r < n and customList[r] < customList[smallest]:
        smallest = r
    
    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)


def heapSort(customList):
    n = len(customList)
    for i in range(int(n/2)-1, -1, -1):
        heapify(customList, n, i)
    
    for i in range(n-1,0,-1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    customList.reverse()


cList = [2,1,3,7,9,8,6,5,4,0]
bubbleSort(cList)
print("---------------------------")
selectionSort(cList)
print("---------------------------")
print(insertionSort(cList))
print("---------------------------")
print(bucketSort(cList))
print("---------------------------")
print(mergeSort(cList, 0, 9))
print("---------------------------")
print(cList)
print("---------------------------")
heapSort(cList)
print(cList)
print("---------------------------")