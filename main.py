from src.graph import Graph
from src.dijkstra import dijkstra
g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)
g.add_edge(3, 4, 3)
dijkstra(g, 0)
