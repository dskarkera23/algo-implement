# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end of the DLL
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    # Insert at the beginning of the DLL
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Delete at the end of the DLL
    def delete_at_end(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.prev.next = None

    # Delete at the beginning of the DLL
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    # Display the doubly linked list
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.display()  # 10 <-> 20 <-> 30 <-> None

dll.insert_at_beginning(5)
dll.display()  # 5 <-> 10 <-> 20 <-> 30 <-> None

dll.delete_at_end()
dll.display()  # 5 <-> 10 <-> 20 <-> None

dll.delete_at_beginning()
dll.display()  # 10 <-> 20 <-> None
