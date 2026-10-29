def a_star(graph, heuristics, start, goal):
    open_list = set([start])
    closed_list = set()

    g = {}
    g[start] = 0

    parents = {}
    parents[start] = start

    while len(open_list) > 0:
        n = None

        for v in open_list:
            if n is None or g[v] + heuristics[v] < g[n] + heuristics[n]:
                n = v

        if n is None:
            print("Path does not exist!")
            return None

        if n == goal:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print("Path found:", path)
            print("Total Cost:", g[goal])
            return path

        for (m, weight) in graph.get(n, []):
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        open_list.remove(n)
        closed_list.add(n)

    print("Path does not exist!")
    return None

graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
    'G': []
}

heuristics = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
}

print("Running A* Search:")
a_star(graph, heuristics, 'A', 'G')
