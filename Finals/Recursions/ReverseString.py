def reverse_string(s):
    if len(s) == 0:
        return s
        
    return reverse_string(s[1:]) + s[0]
    
text = input("Enter a string: ")

print("\n--- Output ---")
print(f"Reversed: {reverse_string(text)}")