from itertools import permutations

def travelling_salesman(graph, start):
    vertices = list(range(len(graph)))
    vertices.remove(start)

    min_cost = float('inf')
    best_path = []

    for perm in permutations(vertices):
        current_cost = 0
        k = start
        current_path = [start]

        for j in perm:
            current_cost += graph[k][j]
            k = j
            current_path.append(j)

        current_cost += graph[k][start]
        current_path.append(start)

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return best_path, min_cost

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_city = 0
path, cost = travelling_salesman(graph, start_city)

print("Distance Matrix:")
for row in graph:
    print(row)
print("Starting City:", start_city)
print("Optimal Path:", path)
print("Minimum Cost:", cost)
