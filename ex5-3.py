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


def test_queue(queue_class, size=5):
    print(f"\nTesting {queue_class.__name__} with size {size}")
    print("-" * 50)
    
    q = queue_class(size)
    operations = [
        (q.peek, [], "peek None"),
        
        (q.dequeue, [], "dequeue None"),
        
        (q.enqueue, [10], "enqueue 10"),
        (q.enqueue, [20], "enqueue 20"),
        (q.enqueue, [30], "enqueue 30"),
        
        (q.peek, [], "peek 10"),
        
        (q.dequeue, [], "dequeue 10"),
        (q.dequeue, [], "dequeue 20"),
        
        (q.enqueue, [40], "enqueue 40"),
        (q.enqueue, [50], "enqueue 50"),
        (q.enqueue, [60], "enqueue 60"),
        
        (q.enqueue, [70], "enqueue 70"),
        
        (q.enqueue, [80], "enqueue None"),
        
        (q.peek, [], "peek 30"),
        
        (q.dequeue, [], "dequeue 30"),
        (q.dequeue, [], "dequeue 40"),
        (q.dequeue, [], "dequeue 50"),
        (q.dequeue, [], "dequeue 60"),
        (q.dequeue, [], "dequeue 70"),
        
        (q.dequeue, [], "dequeue None"),
        
        (q.enqueue, [100], "enqueue 100"),
        (q.enqueue, [200], "enqueue 200"),
        (q.enqueue, [300], "enqueue 300"),
        (q.dequeue, [], "dequeue 100"),
        (q.enqueue, [400], "enqueue 400"),
        (q.enqueue, [500], "enqueue 500"),
        (q.enqueue, [600], "enqueue 600"),  
        (q.enqueue, [700], "enqueue None"),  
        
        (q.peek, [], "peek 200"),
        (q.dequeue, [], "dequeue 200"),
        (q.dequeue, [], "dequeue 300"),
        (q.dequeue, [], "dequeue 400"),
        (q.dequeue, [], "dequeue 500"),
        (q.dequeue, [], "dequeue 600"),
        
        (q.dequeue, [], "dequeue None"),
        (q.peek, [], "peek None"),
        
        (q.enqueue, [999], "enqueue 999"),
        (q.peek, [], "peek 999"),
        (q.dequeue, [], "dequeue 999"),
        (q.dequeue, [], "dequeue None"),
    ]
    
    print("Executing operations:")
    for i, (op, args, expected) in enumerate(operations, 1):
        result = op(*args)
        print(f"{i:2d}. {expected}")
    
    print(f"\nTotal operations: {len(operations)}")

test_queue(CircularArrayQueue, 5)
test_queue(CircularLinkedListQueue, 5)