class TreeNode:
    def __init__(self,data,children = []):
        self.data = data
        self.children = children

    def __str__(self,level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self,TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks',[])
cold = TreeNode('Cold',[])
hot = TreeNode('Hot',[])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode('Tea',[])
coffee = TreeNode('Coffee',[])
cola = TreeNode('Cola',[])
fanta = TreeNode('Fanta',[])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)

# the very first type of tree is - BINARY TREE
# -they are the DS in which each node has at most two children,often reffered to as the left and the right child
# -BINARY TREE is a family of DS (BST , Heap Tree , AVL , Red Black Trees , Syntax Tree)
# - its used to solve a variety of problems like (Huffman coding problem , heap priority problem and expression parsing problem can be solved efficiently using binary trees)

# --Traversing Tree-- #

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
# Four options for tree traversal - DFS(preorder Traversal,inorder traversal,postorder traversal)BFS(levelorder traversal)
leftChild = TreeNode("Hot")
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
cola = TreeNode('Cola')
fanta = TreeNode('Fanta')
rightChild.leftChild = cola
rightChild.rightChild = fanta
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

preOrderTraversal(newBT)
# TC & SC - O(n)
print("------")
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
    
inOrderTraversal(newBT)
# TC & SC - O(n)
print("------")
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
        
postOrderTraversal(newBT)
# TC & SC - O(n)
print("------")
import QueueLinkedList as queue
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

levelOrderTraversal(newBT)
# TC & SC - O(n)
print("------")

def searchBT(rootNode,nodeValue):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "SUCESS"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "NOT FOUND !!"

print(searchBT(newBT, "coffee"))
print("--------------------")
def insertNodeBT(rootNode,newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully Inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully Inserted"

newNode = TreeNode("Lemon Tea")
print(insertNodeBT(newBT, newNode))
levelOrderTraversal(newBT)
# TC & SC - O(n)
print("---------------")
# deletion of a node in Binary Tree
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        # enqueue means put() and dequeue means get()
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        deepestNodes = root.value
        return deepestNodes

def deletionDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.rightChild is dNode:
                root.value.rightChild = None
                return
            else:
                customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild is dNode:
                root.value.leftChild = None
                return
            else:
                customQueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deletionDeepestNode(rootNode, dNode)
                return "The node haas been successfully deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Failed to Delete"

# newNode = getDeepestNode(newBT)
# deletionDeepestNode(newBT, newNode)
deleteNodeBT(newBT, 'Hot')
levelOrderTraversal(newBT)

# TC & SC - O(n)
print("---------------")
# Deletion of entire binary tree
def deleteWholeBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT is successfully deleted"

deleteWholeBT(newBT)
levelOrderTraversal(newBT)
print("----Here we complete Binary Tree with Linked List----")

# Binary Tree using Python List
class BinaryTree():
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

# TC - O(1) & SC - O(n)

    def insertValueBT(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is FULL"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value is successfully inserted"

# TC - O(1) & SC - O(n)

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found"

# TC - O(n) & SC - O(1)

    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)
    
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
    
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])


    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])


    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"

    def deleteBT(self):
       self.customList = None
       return "The BT has been successfully deleted"

newBT = BinaryTree(8)
print(newBT.insertValueBT("--Drinks--"))
print(newBT.insertValueBT("<HOT>"))
print(newBT.insertValueBT("<COLD>"))
print(newBT.insertValueBT("Tea"))
print(newBT.insertValueBT("Coffee"))
print(newBT.insertValueBT("Cola"))
print(newBT.insertValueBT("Fanta"))
print('------------------')
# print(newBT.searchNode("Cold"))
newBT.preOrderTraversal(1)
print('------------------')
newBT.inOrderTraversal(1)
print('------------------')
newBT.postOrderTraversal(1)
print('------------------')
print(newBT.deleteNode("<HOT>"))
print('------------------')
newBT.levelOrderTraversal(1)
print('------------------')
print(newBT.deleteBT())
print('------------------')
