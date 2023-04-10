# -in the left subtree the value of a node is less than or equal to its parent nodes value
# -in the rigth subtree the value of a node is greater than the parent node
# - we need binary subtree because it performs faster than the binary tree in terms of insertion and deletion of nodes

class BSTNode():
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# TC & SC - O(1)


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"

# TC & SC - O(logN) 

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

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
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)


def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data 
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"

newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST, 30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)

print(newBST)
# print(newBST.leftChild.data)
preOrderTraversal(newBST)
print('--------------')
inOrderTraversal(newBST)
print('--------------')
postOrderTraversal(newBST)
print('--------------')
levelOrderTraversal(newBST)
print('--------------')
searchNode(newBST, 80)
print('--------------')
print(deleteBST(newBST))
print('--------------')

# BST using Python List

class BSTNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def insertValueBST(Node,value):
    if value < Node.value:
        if Node.left is None:
            Node.left = BSTNode(value)
        else:
            insertValueBST(Node.left,value)
    else:
        if Node.right is None:
            Node.right = BSTNode(value)
        else:
            insertValueBST(Node.right,value)
    return  "Nodes successfully added"
    
def pre_order_traversal(Node):
    print(Node.value)
    if Node.left:
        pre_order_traversal(Node.left)
    if Node.right:
        pre_order_traversal(Node.right)

def inOrderTraversal(Node):
    if Node.left:
        inOrderTraversal(Node.left)
    print(Node.value)
    if Node.right:
        inOrderTraversal(Node.right)

def postOrderTraversal(Node):
    if Node.left:
        postOrderTraversal(Node.left)
    if Node.right:
        postOrderTraversal(Node.right)
    print(Node.value)
    
# 
    

newBSTPL = BSTNode(0)
insertValueBST(newBSTPL,70)
insertValueBST(newBSTPL,50)
insertValueBST(newBSTPL,90)
insertValueBST(newBSTPL,30)
insertValueBST(newBSTPL,60)
insertValueBST(newBSTPL,80)
insertValueBST(newBSTPL,100)
insertValueBST(newBSTPL,20)
insertValueBST(newBSTPL,40)

print(newBSTPL)
print('------------------')
pre_order_traversal(newBSTPL)
print('------------------')
inOrderTraversal(newBSTPL)
print('------------------')
postOrderTraversal(newBSTPL)
print('------------------')
levelOrderTraversal(newBSTPL)
print('------------------')

