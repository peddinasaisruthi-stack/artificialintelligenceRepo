MAX = 1000
MIN = -1000

def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        best = MIN
        for i in range(0, 2):
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Leaf node values:", values)
result = alpha_beta(0, 0, True, values, MIN, MAX)
print("The optimal value using Alpha-Beta Pruning is:", result)
