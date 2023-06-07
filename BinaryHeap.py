# whats a binary heap ? binary heap is either min heap or max heap. in min binary heap the key at root must be minimum among all key present in binary heap the same property must be recursively true for all nodes in binary tree and viseversa for max heap
# its an complete tree (all levels are completely filled except possibily the last level and the last level has all keys left as possible).this property of binary heap makes them suitable to be stored in an array
# the value of any given node is less then the value of its children its the case of minimum heap 
# in case of max binary heap it is the exact opposite of min heap as the value of each node is more than or equal to both the child node
# binaryy  heap can be implemented using array/ list or refrence/pointer all this implementation are same but we will use array as it fits best
class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0 
        self.maxSize = size + 1

# tc = O(1) & sc = O(N)

def peekofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

# tc = O(1) & sc = O(1)

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

# tc = O(1) & sc = O(1)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])

# tc = O(n) & sc = O(1)

def heapifyTreeInsert(rootNode,index,heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

# tc = O(logN) & sc = O(LogN)

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value is successfully inserted"

# tc = O(logN) & sc = O(LogN)

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return

    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode

# tc = O(logN) & sc = O(LogN)  

def deleteEntireBP(rootNode):
    rootNode.customList = None


newBinaryHeap = Heap(5)
insertNode(newBinaryHeap, 4, "Min")
insertNode(newBinaryHeap, 5, "Min")
insertNode(newBinaryHeap, 2, "Min")
insertNode(newBinaryHeap, 1, "Min")
print("--------")
print(sizeofHeap(newBinaryHeap))
print("--------")
levelOrderTraversal(newBinaryHeap)
print("---------")
extractNode(newBinaryHeap, "Min")
levelOrderTraversal(newBinaryHeap)
insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
print("-------")
levelOrderTraversal(newBinaryHeap)
print("-------")
extractNode(newBinaryHeap, "Max")
levelOrderTraversal(newBinaryHeap)
print("-------")