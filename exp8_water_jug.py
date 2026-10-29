def water_jug_problem(capacity_a, capacity_b, target):
    visited = set()
    queue = []

    queue.append((0, 0, [(0, 0)]))
    visited.add((0, 0))

    while queue:
        a, b, path = queue.pop(0)

        if a == target or b == target:
            print("Steps to solve Water Jug Problem:")
            for step in path:
                print("Jug A:", step[0], "L , Jug B:", step[1], "L")
            return

        operations = [
            (capacity_a, b),
            (a, capacity_b),
            (0, b),
            (a, 0),
            (a - min(a, capacity_b - b), b + min(a, capacity_b - b)),
            (a + min(b, capacity_a - a), b - min(b, capacity_a - a))
        ]

        for state in operations:
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], path + [state]))

capacity_a = 4
capacity_b = 3
target = 2

print("Capacities: Jug A =", capacity_a, "L, Jug B =", capacity_b, "L, Target =", target, "L")
water_jug_problem(capacity_a, capacity_b, target)
