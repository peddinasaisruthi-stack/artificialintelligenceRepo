def objective_function(x):
    return -1 * (x - 5) ** 2 + 25

def hill_climbing(start_x):
    current_x = start_x
    current_val = objective_function(current_x)

    print("Initial State: x =", current_x, "f(x) =", current_val)

    while True:
        left_neighbor = current_x - 1
        right_neighbor = current_x + 1

        left_val = objective_function(left_neighbor)
        right_val = objective_function(right_neighbor)

        next_x = current_x
        next_val = current_val

        if left_val > next_val:
            next_x = left_neighbor
            next_val = left_val

        if right_val > next_val:
            next_x = right_neighbor
            next_val = right_val

        if next_val <= current_val:
            break

        current_x = next_x
        current_val = next_val
        print("Move to: x =", current_x, "f(x) =", current_val)

    print("Peak found at: x =", current_x, "with maximum value f(x) =", current_val)

hill_climbing(0)
