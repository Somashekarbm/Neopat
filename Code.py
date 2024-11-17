Imagine-

def find_first_and_last_position(book_ids, target):
    def find_first():
        left, right = 0, len(book_ids) - 1
        first_index = -1
        while left <= right:
            mid = (left + right) // 2
            if book_ids[mid] == target:
                first_index = mid
                right = mid - 1  # Move left to find the first occurrence
            elif book_ids[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first_index

    def find_last():
        left, right = 0, len(book_ids) - 1
        last_index = -1
        while left <= right:
            mid = (left + right) // 2
            if book_ids[mid] == target:
                last_index = mid
                left = mid + 1  # Move right to find the last occurrence
            elif book_ids[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last_index

    first_index = find_first()
    last_index = find_last()
    return f"{first_index} {last_index}" if first_index != -1 else "NO OCCURRENCES"

# Input Parsing
n = int(input("Enter the total number of book IDs: "))
book_ids = input("Enter the sorted list of book IDs: ").split()
target = input("Enter the specific book ID to find: ")

# Processing and Output
result = find_first_and_last_position(book_ids, target)
print(result)

Ram-

def remove_middle_element(vl, stack_elements):
    # Determine the middle index
    if vl % 2 == 0:  # Even number of elements
        middle_index = (vl // 2) - 1
    else:  # Odd number of elements
        middle_index = vl // 2

    # Remove the middle element
    stack_elements.pop(middle_index)

    # Reverse the stack to simulate stack order and return as a string
    return " ".join(map(str, stack_elements[::-1]))

# Input Parsing
vl = int(input("Enter the number of elements in the stack: "))
stack_elements = list(map(int, input("Enter the stack elements: ").split()))

# Processing
result = remove_middle_element(vl, stack_elements)

# Output
print(result)
