class CircularArrayQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0
    
    def enqueue(self, element):
        if self.count == self.size:
            print(f"enqueue None")
            return
        
        self.queue[self.rear] = element
        print(f"enqueue {element}")
        self.rear = (self.rear + 1) % self.size
        self.count += 1
    
    def dequeue(self):
        if self.count == 0:
            print("dequeue None")
            return None
        
        element = self.queue[self.front]
        print(f"dequeue {element}")
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return element
    
    def peek(self):
        if self.count == 0:
            print("peek None")
            return None
        
        element = self.queue[self.front]
        print(f"peek {element}")
        return element

if __name__ == "__main__":
    q = CircularArrayQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)  
    q.peek()
    q.dequeue()
    q.dequeue()
    q.enqueue(5)
    q.peek()