def dijkstra(graph, start):
    INF = float('inf')
    dist = [INF] * graph.vertices
    visited = [False] * graph.vertices
    dist[start] = 0
    for _ in range(graph.vertices):
        u = -1
        for v in range(graph.vertices):
            if not visited[v] and (u == -1 or dist[v] < dist[u]):
                u = v
        if dist[u] == INF:
            break
        visited[u] = True
        for edge in graph.adj[u]:
            if dist[u] + edge.weight < dist[edge.to]:
                dist[edge.to] = dist[u] + edge.weight
    print(f"\nКратчайшие пути от вершины {start}:")
    for v in range(graph.vertices):
        if dist[v] == INF:
            print(f"Вершина {v}: недостижима")
        else:
            print(f"Вершина {v}: {dist[v]}")