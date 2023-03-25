#   Created by Elshad Karimov on 17/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 1 - Remove Dups : Write a code to remove duplicates from an unsorted linked list. 


from LinkedList import LinkedList
from random import randint
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class LinkedList(LinkedList):
    def __init__(self, values = None):
        self.head = None
        self.tail = None

    def removeDups(self):
        if self.head is None:
            return
        else:
            currentNode = self.head
            visited = set([currentNode.value])
            while currentNode.next:
                if currentNode.next.value in visited:
                    currentNode.next = currentNode.next.next
                else:
                    visited.add(currentNode.next.value)
                    currentNode = currentNode.next
            return self

    def removeDups1(self):
        if self.head is None:
            return
        
        currentNode = self.head
        while currentNode:
            runner = currentNode
            while runner.next:
                if runner.next.value == currentNode.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currentNode = currentNode.next
        return self.head

customLL = LinkedList()
customLL.generate(10, 0, 10)
print(customLL)
customLL.removeDups1()
print(customLL)