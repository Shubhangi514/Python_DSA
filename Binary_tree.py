# class TreeNode:
#     def __init__(self,data,children = []):
#         self.data = data
#         self.children = children

#     def __str__(self,level=0):
#         ret = " " * level + str(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level + 1)
#         return ret

#     def addChild(self,TreeNode):
#         self.children.append(TreeNode)

# tree = TreeNode('Drinks',[])
# cold = TreeNode('Cold',[])
# hot = TreeNode('Hot',[])
# tree.addChild(cold)
# tree.addChild(hot)
# tea = TreeNode('Tea',[])
# coffee = TreeNode('Coffee',[])
# cola = TreeNode('Cola',[])
# fanta = TreeNode('Fanta',[])
# cold.addChild(cola)
# cold.addChild(fanta)
# hot.addChild(tea)
# hot.addChild(coffee)
# print(tree)

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
# TC & SC - O(n)
print("--------------------")
def insertNodeBT(rootNode,newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
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

root = TreeNode("Tea")
print(insertNodeBT(root, TreeNode("Lemon Tea")))
print(insertNodeBT(root, TreeNode("Masala White Tea")))
root = TreeNode("Coffee")
print(insertNodeBT(root, TreeNode("Espresso")))
print(insertNodeBT(root, TreeNode("Latte")))
# newNode = TreeNode("Coca Cola")
# newNode = TreeNode("Thumsup")
# newNode = TreeNode("Orange")
# newNode = TreeNode("Berry")
print(insertNodeBT(newBT, root))
levelOrderTraversal(newBT)
# TC & SC - O(n)
print("--------------------")
