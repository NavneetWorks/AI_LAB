

HUMAN = 'X'
BOT = 'O'
EMPTY = ' '

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6)               # diagonals
]


def print_board(board):
    """Prints the board in a 3x3 grid with cell indices shown for empty cells."""
    print()
    for r in range(3):
        row_cells = []
        for c in range(3):
            i = r * 3 + c
            row_cells.append(board[i] if board[i] != EMPTY else str(i))
        print(f" {row_cells[0]} | {row_cells[1]} | {row_cells[2]} ")
        if r < 2:
            print("---+---+---")
    print()


def check_winner(board):
    for a, b, c in WIN_COMBOS:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return EMPTY not in board


def get_empty_cells(board):
    return [i for i in range(9) if board[i] == EMPTY]


def minimax(board, depth, is_maximizing):
   
    winner = check_winner(board)
    if winner == BOT:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for cell in get_empty_cells(board):
            board[cell] = BOT             
            score = minimax(board, depth + 1, False)
            board[cell] = EMPTY          
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for cell in get_empty_cells(board):
            board[cell] = HUMAN           
            score = minimax(board, depth + 1, True)
            board[cell] = EMPTY          
            best_score = min(best_score, score)
        return best_score


def find_best_move(board):
    
    best_score = float('-inf')
    best_move = None

    for cell in get_empty_cells(board):
        board[cell] = BOT                     
        score = minimax(board, 0, False)       
        board[cell] = EMPTY                  

        print(f"  -> if bot plays {cell}, guaranteed outcome score = {score}")

        if score > best_score:
            best_score = score
            best_move = cell

    return best_move


def human_move(board):
    while True:
        try:
            move = int(input(f"Your move ({HUMAN}) - enter cell 0-8: "))
        except ValueError:
            print("Please enter a number between 0 and 8.")
            continue
        if move not in range(9) or board[move] != EMPTY:
            print("Invalid move, cell taken or out of range. Try again.")
            continue
        return move


def play_game():
    board = [EMPTY] * 9
    print("Welcome to Tic-Tac-Toe! You are 'X', Bot is 'O'.")
    print("Cell positions:")
    print_board(list('012345678'))

    current_player = HUMAN  

    while True:
        print_board(board)

        if check_winner(board):
            break
        if is_full(board):
            break

        if current_player == HUMAN:
            move = human_move(board)
            board[move] = HUMAN
            current_player = BOT
        else:
            print("Bot is thinking (evaluating every move via backtracking)...")
            move = find_best_move(board)
            print(f"Bot chooses cell {move}")
            board[move] = BOT
            current_player = HUMAN

    print_board(board)
    winner = check_winner(board)
    if winner == HUMAN:
        print("You win! 🎉")
    elif winner == BOT:
        print("Bot wins! 🤖")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play_game()
