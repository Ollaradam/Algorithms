def solve_tsp(G):
    visited = []
    solution = []
    src = 0
    while src not in visited:
        solution.append(src)
        edges = G[src]
        weight = 0
        vert = 0
        visited.append(src)
        for (i, j) in enumerate(edges):
            if (weight == 0) and (i not in visited):
                weight = j
                vert = i
            elif (weight != 0) and (j < weight) and (i not in visited):
                weight = j
                vert = i
        if vert != 0:
            src = vert

    solution.append(0)
    print(solution)
    return solution


G = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0],
]
solve_tsp(G)
