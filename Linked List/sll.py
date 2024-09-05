# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to insert a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Method to insert a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to delete a node at the end
    def delete_at_end(self):
        if self.head is None:  # If the list is empty
            print("List is empty.")
            return
        if self.head.next is None:  # If there's only one element
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    # Method to delete a node at the beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty.")
            return
        self.head = self.head.next

    # Method to display the linked list
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()  # 10 -> 20 -> 30 -> None

ll.insert_at_beginning(5)
ll.display()  # 5 -> 10 -> 20 -> 30 -> None

ll.delete_at_end()
ll.display()  # 5 -> 10 -> 20 -> None

ll.delete_at_beginning()
ll.display()  # 10 -> 20 -> None
