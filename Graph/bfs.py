from collections import deque

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            print(node, end=" ")  # Process node (or do any other operation)
            visited.add(node)
            queue.extend(graph[node])  # Add neighbors to queue

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
bfs_iterative(graph, 'A')

