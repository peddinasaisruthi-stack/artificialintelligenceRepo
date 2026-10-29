N = 8

def print_solution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nq_util(board, col + 1):
                return True
            board[i][col] = 0

    return False

def solve_nq():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_nq_util(board, 0):
        print("Solution does not exist")
        return False

    print("8-Queens Solution Matrix:")
    print_solution(board)
    return True

solve_nq()
