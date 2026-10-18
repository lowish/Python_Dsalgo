user_input = input("Enter items to push (space-separated): ")
items = user_input.split()

s = []
for item in items:
    s.append(item)
    
print("\n--- Output ---")
print(f"Final Stack: {s}")