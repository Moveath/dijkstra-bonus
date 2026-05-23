# Dijkstra's Algorithm Bonus Task
## Description
Implementation of Dijkstra's Algorithm in Python to find the shortest path
from a starting vertex to all other vertices in a weighted graph.
## Project Structure
dijkstra-project/
├── src/
│   ├── edge.py       # Edge class with weight field
│   ├── graph.py      # Graph class with adjacency list
│   └── dijkstra.py   # Dijkstra's algorithm implementation
├── main.py           # Example usage and output
└── README.md
## How It Works
1. Set distance to start vertex = 0, all others = infinity
2. Pick the unvisited vertex with the minimum distance
3. Update distances to all its neighbors
4. Mark the vertex as visited
5. Repeat until all vertices are visited
## Classes
**Edge** stores destination vertex and edge weight
**Graph** stores adjacency list of weighted edges
**dijkstra()** implements the algorithm using arrays and simple loops
## Example Output
Shortest paths from vertex 0:
  Vertex 0: 0
  Vertex 1: 3
  Vertex 2: 1
  Vertex 3: 4
  Vertex 4: 7
## How to Run
python main.py
