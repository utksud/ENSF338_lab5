class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedListQueue:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.front = None
        self.rear = None
    
    def enqueue(self, element):
        if self.count == self.size:
            print(f"enqueue None")
            return
        
        new_node = Node(element)
        
        if self.count == 0:
            self.front = new_node
            self.rear = new_node
            new_node.next = new_node
        else:
            self.rear.next = new_node
            new_node.next = self.front
            self.rear = new_node
        
        print(f"enqueue {element}")
        self.count += 1
    
    def dequeue(self):
        if self.count == 0:
            print("dequeue None")
            return None
        
        element = self.front.data
        
        if self.count == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        
        print(f"dequeue {element}")
        self.count -= 1
        return element
    
    def peek(self):
        if self.count == 0:
            print("peek None")
            return None
        
        element = self.front.data
        print(f"peek {element}")
        return element

if __name__ == "__main__":
    q = CircularLinkedListQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)  
    q.peek()
    q.dequeue()
    q.dequeue()
    q.enqueue(5)
    q.peek()