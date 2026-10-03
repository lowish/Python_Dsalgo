class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def rear(self):
        if not self.is_empty():
            return self.items[-1]

    def display(self):
        print(f"Queue Now: {self.items}")

    def is_empty(self):
        return len(self.items) == 0

q = Queue()
for _ in range(3):
    item = input("Enter item to enqueue: ")
    q.enqueue(item)

q.dequeue()

print("\n--- Output ---")
print(f"Front: {q.front()}")
print(f"Rear: {q.rear()}")
q.display()