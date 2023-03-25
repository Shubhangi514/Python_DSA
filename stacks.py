class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self,value):
        self.list.append(value)
        return "the element has been successfully inserted"

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is no such List"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is no such List"
        else:
            return self.list[len(self.list)-1]
        
    # delete
    def delete(self):
        self.list = None

customStack = Stack() 
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
# print(customStack)
# print(customStack.pop())
print(customStack.peek())
# print(customStack.delete())

# Stack with limit

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
      
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # isFull

    def isFull(self):
        if len(self.list) >= self.maxSize:
            return True
        else:
            return False

    # push (TC-amortized)

    def push(self,value):
        if self.isFull():
            return 'the stack is full'
        else:
            self.list.append(value)
            return 'the element has been successfully inserted'

    # pop

    def pop(self):
        if self.isEmpty():
            return "There is no such List"
        else:
            return self.list.pop()

    # peek

    def peek(self): 
        if self.isEmpty():
            return "There is no such List"
        else:
            return self.list[len(self.list)-1]

    # delete
    def delete(self):
        self.list = None



customStack = Stack(3)
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(6)
print(customStack.isFull()) 
print(customStack)

# Operation on Stack using Linked List

class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next    

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peep(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    def delete(self):
        self.LinkedList.head = None
        return "None"

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
# print(customStack.isEmpty())
# print(customStack)
# print("------------")
# customStack.pop()
# print(customStack)
print(customStack.peep())
customStack.delete()
print(customStack)

# # when to use /avoid Stacks
# Use:
# - LIFO functinality
# - The chance of data corruption is minimum
# Avoid:
# -Random access is not possible