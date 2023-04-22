def Prims(G):
    dist = {}
    prev = {}
    visited = []
    MST = []
    s = 0

    for v in range(len(G)):
        dist[v] = float('inf')
        prev[v] = None

    dist[s] = 0
    prev[s] = s

    for node in range(len(G[s])):
        if G[s][node] != 0:
            dist[node] = G[s][node]
            prev[node] = s

    while len(visited) < len(G):
        current_node = None
        small_dist = float('inf')
        for v in dist:
            if v not in visited and dist[v] < small_dist:
                current_node = v
                small_dist = dist[v]
        MST.append((prev[current_node], current_node, small_dist))
        visited.append(current_node)
        for node in range(len(G[current_node])):
            if G[current_node][node] != 0 and node not in visited:
                if G[current_node][node] < dist[node]:
                    dist[node] = G[current_node][node]
                    prev[node] = current_node
    del MST[0]
    # Returned is each tuple for the edge in the MST (previous to current, current node position, smallest distance)
    return MST


G = [
    [0, 8, 5, 0, 0, 0, 0],
    [8, 0, 10, 2, 18, 0, 0],
    [5, 10, 0, 3, 0, 16, 0],
    [0, 2, 3, 0, 12, 30, 14],
    [0, 18, 0, 12, 0, 0, 4],
    [0, 0, 16, 30, 0, 0, 26],
    [0, 0, 0, 14, 4, 26, 0]
]

print(Prims(G))
