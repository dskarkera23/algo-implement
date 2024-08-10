class Node:
   def __init__(self, val):
      self.left = None
      self.right = None
      self.val = val

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val,end=' ')
    inorder(root.right)

def preorder(root):
    if root is None:
        return

    print(root.val,end=' ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
   
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder")
inorder(root)
print("\nPreorder")
preorder(root)
print("\nPostorder")
postorder(root)

"""
Output:
Inorder
4 2 5 1 3
Preorder
1 2 4 5 3
Postorder
4 5 2 3 1

Traversal Summary:

1. Inorder Traversal (LNR):
   - Order: Left -> Root -> Right
   - Time Complexity: O(n)
   - Space Complexity: O(h) where h is the height of the tree (O(log n) for balanced trees, O(n) for skewed trees)

2. Preorder Traversal (NLR):
   - Order: Root -> Left -> Right
   - Time Complexity: O(n)
   - Space Complexity: O(h) where h is the height of the tree (O(log n) for balanced trees, O(n) for skewed trees)

3. Postorder Traversal (LRN):
   - Order: Left -> Right -> Root
   - Time Complexity: O(n)
   - Space Complexity: O(h) where h is the height of the tree (O(log n) for balanced trees, O(n) for skewed trees)
"""
