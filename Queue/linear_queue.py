class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0
    
    def print_ele(self):
        for i in self.queue:
            print(i, end=" ")

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.print_ele()
queue.dequeue()
queue.dequeue()
print("\n")
queue.print_ele()

"""
Output:
10 20 30 
30

Time and Space Complexities:
1. enqueue(item):
   - Time Complexity: O(1)
   - Space Complexity: O(1)

2. dequeue():
   - Time Complexity: O(n)
   - Space Complexity: O(1)

3. peek():
   - Time Complexity: O(1)
   - Space Complexity: O(1)

4. is_empty():
   - Time Complexity: O(1)
   - Space Complexity: O(1)

5. print_ele():
   - Time Complexity: O(n)
   - Space Complexity: O(
"""