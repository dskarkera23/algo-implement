# Tree Traversal Algorithms

This repository contains implementations of three fundamental tree traversal algorithms in Python: Inorder, Preorder, and Postorder traversal. Each algorithm has its own unique way of visiting nodes in a binary tree.

## Traversal Methods

| Traversal  | Shortcut | Order | Time Complexity | Space Complexity |
|------------|----------|-------|-----------------|------------------|
| Inorder    | LNR      | Left -> Node -> Right  | O(n)            | O(h) (O(log n) for balanced trees, O(n) for skewed trees) |
| Preorder   | NLR      | Node -> Left -> Right  | O(n)            | O(h) (O(log n) for balanced trees, O(n) for skewed trees) |
| Postorder  | LRN      | Left -> Right -> Node  | O(n)            | O(h) (O(log n) for balanced trees, O(n) for skewed trees) |

- **n**: Number of nodes in the tree.
- **h**: Height of the tree.
