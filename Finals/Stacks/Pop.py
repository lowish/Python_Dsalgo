user_input = input("Enter items in the stack (space-separated): ")
stack = user_input.split()

popped_element = stack.pop() if stack else None

print("\n--- Output ---")
print(f"Popped Element: {popped_element}")
print(f"Updated Stack: {stack}")