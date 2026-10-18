postfix = input("Enter postfix expression: ")

stack = []
for char in postfix:
    if char.isdigit():
        stack.append(int(char))
    else:
        val2 = stack.pop()
        val1 = stack.pop()
        
        if char == '+':
            stack.append(val1 + val2)
        elif char == '-':
            stack.append(val1 - val2)
        elif char == '*':
            stack.append(val1 * val2)
        elif char == '/':
            stack.append(int(val1 / val2))
print("\n--- Output ---")
print(f"Evaluated Result: {stack[0]}")