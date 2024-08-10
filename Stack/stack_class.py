class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            return item
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0
    
    def print_ele(self):
        for i in self.stack:
            print(i, end=" ")

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(20)
stack.print_ele()
ele = stack.peek()
print("\nLast ele", ele)
stack.pop()   
stack.pop()   
stack.print_ele()

"""
Output:
10 20 20 
Last ele 20
10
"""

"""
Time and Space Complexities:
1. push(item):
   - Time Complexity: O(1)
   - Space Complexity: O(1)

2. pop():
   - Time Complexity: O(1)
   - Space Complexity: O(1)

3. peek():
   - Time Complexity: O(1)
   - Space Complexity: O(1)

4. is_empty():
   - Time Complexity: O(1)
   - Space Complexity: O(1)

5. print_ele():
   - Time Complexity: O(n)
   - Space Complexity: O(1)
"""
