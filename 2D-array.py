import os
from array import *
import numpy as np
twoDarray = np.array(([11,12,13,15,6],[10,9,8,7,1],[12,17,15,8,2],[21,22,23,34,4]))
print(twoDarray)
newTDarray = np.insert(twoDarray,2,[[1,2,3,4]],axis=1)
newTwoDarray = np.append(twoDarray, [[1,2,3,4,5]] , axis=0)
def accessElements(array, rowIndex,colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect index')
    else:
        print(array[rowIndex][colIndex])
accessElements(twoDarray, 2, 3)
def traverseTDarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseTDarray(twoDarray)

def searchTDarray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'the value is located in the index '+str(i)+"   "+str(j)
    return 'the element does not exist'
print(searchTDarray(twoDarray, 75)) 

newTDArray = np.delete(twoDarray,0,axis=0)
print(newTDArray)