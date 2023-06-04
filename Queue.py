class Queue:
    def __init__(self):
        self.item = []

    def __str__(self):
        values = [str(x) for x in self.item]
        return ' '.join(values)

    def isEmpty(self):
        if self.item == []:
            return True
        else:
            return False
    
    def enqueue(self,value):
        self.item.append(value)
        return "The element is inserted at the end od Queue"
	
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.item.pop(3)

    def peek(self):
        if self.isEmpty():
            return "There is no such List"
        else:
            return self.item[0]


    def delete(self):
        self.list = None


customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
customQueue.enqueue(5)
print("--------------------------")
# customQueue.peek()
print(customQueue.dequeue())
print(customQueue)
print("--------------------------")
customQueue.delete()
print(customQueue)
print("--------------------------")

# Circular Queue

class Queue:
    def __init__(self,maxSize):
        self.items = maxSize * [None] #we need to initialize all sets to none
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return "The  Queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

customQueue = Queue(5)
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue.isFull())
customQueue.dequeue()
print(customQueue.peek())
print(customQueue.delete())
print(customQueue)



# collection module

from collections import deque

customQueue = deque(maxlen=3) 
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)
print(customQueue)
print(customQueue.clear())
print(customQueue)

# # queue module

import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())

# multiprocessing module

from multiprocessing import Queue

customQueue = Queue(maxsize= 3)
customQueue.put(1)
print(customQueue.get())