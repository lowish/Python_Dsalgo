stack = []

stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')

print(f"Stack: {stack}")

removed1 = stack.pop()
print(f"Removed: {removed1}")

removed2 = stack.pop()
print(f"Removed: {removed2}")

print(f"Remaining Stack: {stack}")

print()

queue = []

queue.append('A')
queue.append('B')
queue.append('C')
queue.append('D')

print(f"Queue: {queue}")

removed_q1 = queue.pop(0)
print(f"Removed: {removed_q1}")

removed_q2 = queue.pop(0)
print(f"Removed: {removed_q2}")

print(f"Remaining Queue: {queue}")