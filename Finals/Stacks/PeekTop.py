user_input = input("Enter items in the stack (space-separated): ")
stack = user_input.split()

top_element = stack[-1] if stack else None

print("\n--- Output ---")
print(f"Top Element: {top_element}")
print(f"Current Stack: {stack}")