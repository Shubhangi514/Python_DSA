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
            return self.item.pop(0)

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
print(customQueue.dequeue())
print(customQueue)
customQueue.delete()
print(customQueue)