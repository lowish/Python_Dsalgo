queue = input("Enter queue items (space-separated): ").split()
print("\n--- Output ---")
if queue:
    print(f"Front: {queue[0]}")
    print(f"Rear: {queue[-1]}")