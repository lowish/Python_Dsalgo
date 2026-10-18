infix = input("Enter infix expression: ")

precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
stack = []
postfix = []
for char in infix:
    if char.isalnum():
        postfix.append(char)
    elif char == '(':
        stack.append(char)
    elif char == ')':
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()  # Remove '('
    else:
        while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
            postfix.append(stack.pop())
        stack.append(char)

while stack:
    postfix.append(stack.pop())

print("\n--- Output ---")
print(f"Postfix Expression: {''.join(postfix)}")