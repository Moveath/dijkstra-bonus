from src.edge import Edge
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[] for _ in range(vertices)]
    def add_edge(self, from_v, to_v, weight):
        self.adj[from_v].append(Edge(to_v, weight))
        self.adj[to_v].append(Edge(from_v, weight))