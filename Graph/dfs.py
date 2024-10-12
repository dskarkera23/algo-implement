def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end=" ")  # Process node (or do any other operation)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        
        if node not in visited:
            print(node, end=" ")  # Process node (or do any other operation)
            visited.add(node)
            stack.extend(reversed(graph[node]))  # Add neighbors to stack


            
# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs_recursive(graph, 'A')
print()
dfs_iterative(graph, 'A')