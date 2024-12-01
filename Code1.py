you are working-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method to insert data at the end of the linked list
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Method to display the linked list elements
    def display(self):
        current_node = self.head
        timestamps = []
        while current_node:
            timestamps.append(str(current_node.data))
            current_node = current_node.next
        print(" ".join(timestamps))

# Function to sort the timestamps and insert into the linked list
def sort_ticket_requests(n, timestamps):
    linked_list = LinkedList()

    # Insert each timestamp into the linked list
    for timestamp in timestamps:
        linked_list.insert(timestamp)

    # Convert linked list to a list for sorting
    current_node = linked_list.head
    timestamp_list = []
    while current_node:
        timestamp_list.append(current_node.data)
        current_node = current_node.next

    # Sort the timestamps
    timestamp_list.sort()

    # Insert the sorted timestamps back into the linked list
    linked_list = LinkedList()
    for timestamp in timestamp_list:
        linked_list.insert(timestamp)

    # Display the sorted linked list
    linked_list.display()

# Main Function
def main():
    # Reading input
    n = int(input())  # Number of ticket requests
    timestamps = list(map(int, input().split()))  # Ticket request timestamps

    # Sort and display the sorted timestamps
    sort_ticket_requests(n, timestamps)

# Calling main to run the program
if __name__ == "__main__":
    main()


an automated-

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        
        # Level-order insertion
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            
            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def reverse_level_order(self):
        if not self.root:
            return []
        
        # Standard level-order traversal
        queue = deque([self.root])
        result = []
        
        while queue:
            current = queue.popleft()
            result.append(current.data)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        # Return the reverse of the result
        return result[::-1]
    

def main():
    # Read input
    n = int(input())  # Number of product categories
    categories = list(map(int, input().split()))  # Product category IDs

    # Create a binary tree and insert the categories
    tree = BinaryTree()
    
    for category in categories:
        tree.insert(category)
    
    # Get the reverse level order traversal
    reverse_level_order = tree.reverse_level_order()
    
    # Print the result
    print(" ".join(map(str, reverse_level_order)))

# Calling main to run the program
if __name__ == "__main__":
    main()
