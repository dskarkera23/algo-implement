# Heap Data Structure

## Overview
A **heap** is a specialized complete binary tree-based data structure used primarily for priority queues and sorting. It can be of two types:
1. **Min-Heap**: The smallest element is at the root.
2. **Max-Heap**: The largest element is at the root.

### Key Properties
- **Complete Binary Tree**: Every level of the heap is fully filled except possibly the last, which is filled from left to right.
- **Heap Property**: 
  - **Min-Heap**: Parent nodes are smaller than or equal to their children.
  - **Max-Heap**: Parent nodes are larger than or equal to their children.

## Common Operations and Complexities

| Operation         | Time Complexity | Space Complexity |
|-------------------|-----------------|------------------|
| Insert            | O(log n)        | O(1)             |
| Delete Root       | O(log n)        | O(1)             |
| Heapify           | O(log n)        | O(1)             |
| Build Heap        | O(n)            | O(1)             |
| Peek (Get Min/Max)| O(1)            | O(1)             |

### Explanation of Operations
- **Insert**: Adds a new element to the heap and maintains the heap property.
- **Delete Root**: Removes the root element (min in a min-heap, max in a max-heap) and restores the heap property.
- **Heapify**: Ensures the subtree rooted at a node follows the heap property.
- **Build Heap**: Constructs a heap from an unsorted array.
- **Peek**: Returns the smallest element in a min-heap or the largest in a max-heap.

## Applications of Heaps
- **Priority Queues**: Efficiently manage elements with different priorities.
- **Heap Sort**: Sorting algorithm with O(n log n) time complexity.
- **Dijkstra's Algorithm**: Used to find the shortest path in a graph.
- **Job Scheduling**: Assign jobs based on priority.

## Summary
Heaps are efficient for operations that require quick access to the minimum or maximum element. Their structure allows for logarithmic time insertions and deletions, making them suitable for real-time scheduling and resource management systems.
