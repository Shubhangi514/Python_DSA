# linked list is a form of a sequential collecction and it does not have to be in order . A linked list is made up of independent nodes that may contain any type of data and each node has a refrence to the next node in the link
# each node is independent (node : data & link)
# the nodes of linked list are not contagious
# variable size in linked list
# insertion and deletion are very efficient
# iteration is difficult and time consuming
# random access - accessing an element is very efficient in array but difficult in linked in linked list

# TYPES of LINKED LIST:(singly linked list)(circular linked list)(doubly linked list)(circular doubly linked list)

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class SLinkedlist:
    def __init__(self):
        self.head = None #O(1)
        self.tail = None #O(1)
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    def insertSLL(self , value , location):
        newNode = Node(value)
        # nextNode = Node()
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
# INSERTION TO LINKED LIST IN MEMORY:(1.At the beginning of the linked list)(2.After a node in the middle of linked list)(3.At the end of the linked list) 

# traversing singly linked list

    def traverseSLL(self):
        if self.head is None:
            print('The Singly Linked List does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next 
# traversing ka time complexity - O(n) & space complexity - O(1)

# Seearch for value in Single Linked List

    def searchSLL(self, nodeValue):
        if self.head is None:
            return 'The list does not exist'
        else:
            node = self.head 
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"
# time complexity - O(n) space Complexity - O(1)

# deletion of node from singly linked list

    def deleteNode(self,location):
        if self.head is None :
            return "the value already dont exist"
        else :
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:       # deleting the last node 
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node 
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
# time complexity - O(n) & space complexity - O(1)

# deletion of an entire linked list

    def deleteEntireSLL(self):
        if self.head is None:
            print('SLL alrady DNE')
        else:
            self.head = None
            self.tail = None
# time complexity - O(1) & space complexity - O(1)

                
# singlyLinkedList = SLinkedlist()
# node1 = Node(1) #O(1)
# node2 = Node(2) #O(1)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2 #O(1)
# singlyLinkedList.tail = node2 
# overall TC & SC is #O(1)

singlyLinkedList = SLinkedlist()
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(5,1)
singlyLinkedList.insertSLL(6,1)

singlyLinkedList.insertSLL(0,0)

singlyLinkedList.insertSLL(0,3)
singlyLinkedList.insertSLL(0,6)
print([node.value for node in singlyLinkedList])
# singlyLinkedList.deleteNode(3)
singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])
# singlyLinkedList.traverseSLL()
# print(singlyLinkedList.searchSLL(4))


# time complexity - O(n) space complexity - O(1)

