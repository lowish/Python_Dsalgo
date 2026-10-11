queue = input("Enter queue items (space-separated): ").split()
print("\n--- Output ---")
if queue:
    dequeued_item = queue.pop(0)
    print(f"Dequeued Item: {dequeued_item}")
print(f"Updated Queue: {queue}")