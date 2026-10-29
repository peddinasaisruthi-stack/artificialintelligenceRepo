board = [' ' for _ in range(9)]

def print_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_draw():
    return ' ' not in board

def play_game():
    current_player = 'X'
    sample_moves = [1, 5, 2, 9, 3]
    use_sample = False

    print("Tic-Tac-Toe Game")
    print_board()

    while True:
        pos = -1
        if not use_sample:
            try:
                move = input("Player " + current_player + ", enter position (1-9): ")
                pos = int(move) - 1
            except (EOFError, ValueError):
                use_sample = True

        if use_sample:
            if not sample_moves:
                break
            pos = sample_moves.pop(0) - 1
            print("Player " + current_player + " places on position " + str(pos + 1))

        if pos < 0 or pos > 8 or board[pos] != ' ':
            print("Invalid move. Try again.")
            continue

        board[pos] = current_player
        print_board()

        if check_win(current_player):
            print("Player " + current_player + " wins!")
            break

        if check_draw():
            print("The game is a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()
