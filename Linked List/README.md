## Types of Linked Lists

### 1. Singly Linked List (SLL)

A **Singly Linked List** is a linear data structure where each element (node) points to the next node, and the last node points to `None`. It only supports forward traversal.

#### Operations:
- **Insert at the end**: Adds a new node to the end of the list.
- **Insert at the beginning**: Adds a new node to the start of the list.
- **Delete at the end**: Removes the node at the end of the list.
- **Delete at the beginning**: Removes the node at the start of the list.
- **Display**: Prints the elements of the linked list.

#### Time Complexities:
| Operation              | Time Complexity |
|------------------------|-----------------|
| Insertion at Beginning  | O(1)            |
| Insertion at End        | O(n)            |
| Deletion at Beginning   | O(1)            |
| Deletion at End         | O(n)            |
| Traversal/Display       | O(n)            |

---

### 2. Doubly Linked List (DLL)

A **Doubly Linked List** is a more complex structure where each node points to both the next node and the previous node, allowing bidirectional traversal.

#### Operations:
- **Insert at the end**: Adds a new node to the end of the list.
- **Insert at the beginning**: Adds a new node to the start of the list.
- **Delete at the end**: Removes the node at the end of the list.
- **Delete at the beginning**: Removes the node at the start of the list.
- **Display**: Prints the elements of the doubly linked list in both directions.

#### Time Complexities:
| Operation              | Time Complexity |
|------------------------|-----------------|
| Insertion at Beginning  | O(1)            |
| Insertion at End        | O(n)            |
| Deletion at Beginning   | O(1)            |
| Deletion at End         | O(n)            |
| Traversal/Display       | O(n)            |

---

### 3. Circular Linked List (CLL)

In a **Circular Linked List**, the last node points back to the head of the list, forming a circular structure. This structure can be singly linked or doubly linked.

#### Operations:
- **Insert at the end**: Adds a new node to the end of the list (which points back to the head).
- **Insert at the beginning**: Adds a new node to the start of the list (while updating the last node to point to the new head).
- **Delete at the end**: Removes the last node and updates the new last node to point to the head.
- **Delete at the beginning**: Removes the head and updates the last node to point to the new head.
- **Display**: Prints the elements of the circular linked list starting from the head and looping back to it.

#### Time Complexities:
| Operation              | Time Complexity |
|------------------------|-----------------|
| Insertion at Beginning  | O(1)            |
| Insertion at End        | O(n)            |
| Deletion at Beginning   | O(1)            |
| Deletion at End         | O(n)            |
| Traversal/Display       | O(n)            |

---