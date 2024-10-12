# Graph Data Structure

## Overview
A **graph** is a collection of nodes (**vertices**) connected by edges. Graphs are used to represent networks of various types, such as social networks, communication systems, or transportation routes.

### Key Types of Graphs
- **Directed Graph (Digraph)**: Edges have a direction, meaning they go from one vertex to another.
- **Undirected Graph**: Edges have no direction, and the connection between vertices is bidirectional.
- **Weighted Graph**: Edges have weights associated with them, representing costs, distances, or any measurable relationship.
- **Unweighted Graph**: Edges do not carry any weight.
- **Cyclic Graph**: A graph that contains at least one cycle (a path that starts and ends at the same vertex).
- **Acyclic Graph**: A graph with no cycles.

## Graph Representation
Graphs can be represented in two common ways:
1. **Adjacency Matrix**: A 2D array where each element represents the presence (and possibly weight) of an edge between vertices.
2. **Adjacency List**: A list where each vertex stores a list of its adjacent vertices.

### Time and Space Complexities for Operations

| Operation                  | Adjacency List | Adjacency Matrix |
|----------------------------|----------------|------------------|
| Add Vertex                 | O(1)           | O(n²)            |
| Add Edge                   | O(1)           | O(1)             |
| Remove Vertex              | O(V + E)       | O(n²)            |
| Remove Edge                | O(E)           | O(1)             |
| Check if Edge Exists       | O(V)           | O(1)             |
| Graph Traversal (DFS/BFS)   | O(V + E)       | O(V²)            |

**V**: Number of vertices  
**E**: Number of edges  
**n**: Size of the graph

### Graph Traversal Algorithms

- **Breadth-First Search (BFS)**: Explores all neighbors of a vertex before moving on to the next level of vertices.
  - Time Complexity: **O(V + E)**
  - Space Complexity: **O(V)**

- **Depth-First Search (DFS)**: Explores as far along a branch as possible before backtracking.
  - Time Complexity: **O(V + E)**
  - Space Complexity: **O(V)**

### Graph Applications
- **Shortest Path**: Algorithms like Dijkstra’s and Bellman-Ford are used to find the shortest path in weighted graphs.
- **Network Flow**: Ford-Fulkerson and Edmonds-Karp algorithms find the maximum flow in a flow network.
- **Topological Sorting**: Used for scheduling tasks where certain tasks must be performed before others.
- **Graph Coloring**: Used in problems like register allocation in compilers.

## Summary
Graphs are a fundamental data structure for representing relationships between entities. With different traversal methods and representation techniques, they can efficiently solve problems related to connectivity, flow, and optimization in both weighted and unweighted scenarios.
