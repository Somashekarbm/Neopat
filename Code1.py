naren-

def is_matching_pair(opening, closing):
    # Check if the pair of brackets matches
    return (opening == '(' and closing == ')') or \
           (opening == '{' and closing == '}') or \
           (opening == '[' and closing == ']')

def are_brackets_balanced(expression):
    stack = []
    
    for char in expression:
        # Push opening brackets onto the stack
        if char in "({[":
            stack.append(char)
        # For closing brackets, check if the stack is empty or mismatched
        elif char in ")}]":
            if not stack or not is_matching_pair(stack.pop(), char):
                return False
    
    # If stack is empty, brackets are balanced
    return len(stack) == 0

# Input
expression = input("Enter the expression: ")

# Output the result
print(f"Expression: {expression}")
if are_brackets_balanced(expression):
    print("Brackets are balanced")
else:
    print("Brackets are not balanced")


neha-

def count_occurrences(s, c, index=0, count=0):
    # Base case: If we reach the end of the string
    if index == len(s):
        return count
    
    # Increment count if the character matches
    if s[index] == c:
        count += 1
    
    # Recursive call to check the next character
    return count_occurrences(s, c, index + 1, count)

# Input
string = input("Enter the string: ")
char = input("Enter the character to count: ")

# Ensure the input character is valid
if len(char) != 1:
    print("Error: Please enter a single character.")
else:
    # Call the function and print the result
    result = count_occurrences(string, char)
    print(f"The character '{char}' appears {result} times.")


