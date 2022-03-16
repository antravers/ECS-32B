# 1
class QueueX():
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# 2, 3, 4
class Node:
    
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return self.head == None

# adds a new item to the end of the list
    def append(self, item):
        temp = Node(item)
        if self.count == 0:
            self.head = temp
        else:
            self.tail.setNext(temp)
        self.tail = temp
        self.count = self.count + 1

# returns the position of item in the list
    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
                return index
            else:
                current = current.getNext()
                index = index + 1
        return found

# adds a new item to the list at position pos        
    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 0
        found = False
        while current != None:
            if count == pos:
                found = True
                break
            else:
                previous = current
                current.setData(current.getNext())
                count = count + 1
        
        while found == True:
            temp = Node(item)
            if self.count == 0:
                temp.setNext(self.head)
                self.head = temp
            else:
                temp.setNext(current)
                previous.setNext(temp)
        self.count = self.count + 1

# removes and returns the last item in the list
# removes and returns the item at position pos
    def pop(self, pos = -1):
        current = self.head
        previous = None
        count = 0
        found = False
        if pos < 0:
            temp = self.head
            while temp.getNext() != None:
                previous = temp
                temp = temp.getNext()
            temp.setNext(None)
            previous.setNext(None)
            self.tail = temp.getNext()
        if pos >= 0:
            while current != None and not found:
                if count == pos:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
                    count = count + 1
        
            while found == True:
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                
      
# return a copy of the list starting at the start position
# and going up but not including the stop position
    def slice(self, start, stop):
        stop = stop - 1
        current = self.head
        count = 1
        while current != None:
            if count == start:
                break
            else:
                current.setData(current.getNext())
                count = count + 1
        temp = Node(current.getData())
        front = temp
        rear = front
        while count < stop:
            current = current.getNext()
            temp = Node(current.getData())
            rear.setNext(temp)
            rear = rear.getNext()
            count = count + 1

        return front

# Unordered linked list to Python list
    def convert(self):
        current = self.head
        previous = None
        list = []
        while True:
            list.append(current)
            if current.getNext() == None:
                break
            current = current.getNext()
        print(list)

# 5
class Stack:
    
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.head == None

    def push(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.count = self.count + 1

    def pop(self):
        temp = self.head
        self.head = self.head.getNext()
        temp.setNext(None)
        self.count = self.count - 1
        return temp
        
    def peek(self):
        return self.head.getData()

    def size(self):
        return self.count

# 6
class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return self.head == None

    def enqueue(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = self.head
        else:
            self.tail.setNext(temp)
            self.tail = self.tail.getNext()
        self.count = self.count + 1

    def dequeue(self):
        if self.isEmpty():
            return None
        temp = self.head

        if self.head.getNext() == None:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.getNext()
        self.count = self.count - 1
        return temp
        
    def size(self):
        return self.count

# 7
class Deque2():

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return self.head == None

    def addFront(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = self.head
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)
        self.count = self.count + 1

    def addRear(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = self.head
        else:
            temp.setNext(self.head)
            self.head = temp
        self.count = self.count + 1

    def removeFront(self):
        temp = self.head
        self.head = self.head.getNext()
        self.count = self.count - 1

    def removeRear(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        previous.setNext(current.getNext())
        self.count = self.count - 1

    def size(self):
        return self.count  
