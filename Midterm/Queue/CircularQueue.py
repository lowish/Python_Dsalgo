class CircularQueue:
    def __init__(self, size=5):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            return  
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            return None  
        
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

cq = CircularQueue(5)

for _ in range(5):
    val = input("Enter value to enqueue: ")
    cq.enqueue(val)

cq.dequeue()
cq.dequeue()

print("\n--- Output ---")
print(f"Queue State: {cq.queue}")