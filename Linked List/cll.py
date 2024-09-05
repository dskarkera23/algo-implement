# Node class for Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end of the CLL
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head

    # Insert at the beginning of the CLL
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        new_node.next = self.head
        self.head = new_node
        last_node.next = self.head

    # Delete at the end of the CLL
    def delete_at_end(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next == self.head:  # Only one element in the list
            self.head = None
            return
        second_last = self.head
        while second_last.next.next != self.head:
            second_last = second_last.next
        second_last.next = self.head

    # Delete at the beginning of the CLL
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next == self.head:  # Only one element in the list
            self.head = None
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        self.head = self.head.next
        last_node.next = self.head

    # Display the circular linked list
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        current_node = self.head
        while True:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print("(head)")

# Example usage
cll = CircularLinkedList()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.display()  # 10 -> 20 -> 30 -> (head)

cll.insert_at_beginning(5)
cll.display()  # 5 -> 10 -> 20 -> 30 -> (head)

cll.delete_at_end()
cll.display()  # 5 -> 10 -> 20 -> (head)

cll.delete_at_beginning()
cll.display()  # 10 -> 20 -> (head)
