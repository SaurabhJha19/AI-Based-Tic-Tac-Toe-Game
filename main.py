import math

def board(Gboard):
    for i in range(3):
        print("|".join(Gboard[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

def move(Gboard, position, player):
    if Gboard[position] == " ":
        Gboard[position] = player
        return True
    return False

def win(Gboard, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(Gboard[i] == player for i in condition):
            return True
    return False

def draw(Gboard):
    return " " not in Gboard

def switch(current):
    return "O" if current == "X" else "X"
    
def project():
    print("A Program by Saurabh Jha")


def minimax(Gboard, depth, alpha, beta, is_maximizing, ai_player, human_player):
    if win(Gboard, ai_player):
        return 1
    elif win(Gboard, human_player):
        return -1
    elif draw(Gboard):
        return 0
    
    if is_maximizing:
        max_best_score = -math.inf
        for i in range(9):
            if Gboard[i] == " ":
                Gboard[i] = ai_player
                score = minimax(Gboard, depth + 1, alpha, beta, False, ai_player, human_player)
                Gboard[i] = " "
                max_best_score = max(score, max_best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return max_best_score
    else:
        min_best_score = math.inf
        for i in range(9):
            if Gboard[i] == " ":
                Gboard[i] = human_player
                score = minimax(Gboard, depth + 1, alpha, beta, True, ai_player, human_player)
                Gboard[i] = " "
                min_best_score = min(score, min_best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return min_best_score
    
def ai_move(Gboard, ai_player, human_player):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if Gboard[i] == " ":
            Gboard[i] = ai_player
            score = minimax(Gboard, 0, -math.inf, math.inf, False, ai_player, human_player)
            Gboard[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


def player_vs_player():
    Game_board = [" " for _ in range(9)]
    current = "X"

    while True:
        board(Game_board)
        try:
            try_move = int(input(f"Player {current}, enter your move (1-9): ")) - 1
            if try_move < 0 or try_move > 8 or Game_board[try_move] != " ":
                print("Invalid move, try again.")
                continue
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue
        
        Game_board[try_move] = current

        if win(Game_board, current):
            board(Game_board)
            print(f"Player {current} wins!")
            break

        if draw(Game_board):
            board(Game_board)
            print("It's a draw!")
            break

        current = "O" if current == "X" else "X"


def player_vs_ai():
    Game_board = [" " for _ in range(9)]

    human_player = input("Do you want to be X or O? ").upper()
    while human_player not in ["X", "O"]:
        human_player = input("Invalid choice. Please choose X or O: ").upper()

    ai_player = "O" if human_player == "X" else "X"

    current = "X"

    while True:
        board(Game_board)
        if current == human_player:
            try:
                try_move = int(input(f"Player {current}, enter your move (1-9): ")) - 1
                if try_move < 0 or try_move > 8 or Game_board[try_move] != " ":
                    print("Invalid move, try again.")
                    continue
            except ValueError:
                print("Please enter a number between 1 and 9.")
                continue

            Game_board[try_move] = current

        else:
            print("AI is making a move --->")
            try_move = ai_move(Game_board, ai_player, human_player)
            Game_board[try_move] = ai_player

        if win(Game_board, current):
            board(Game_board)
            if current == human_player:
                print(f"Player wins!")
            
            else:
                print(f"System wins!")
            break
        elif draw(Game_board):
            board(Game_board)
            print("It's a draw!")
            break

        current = "O" if current == "X" else "X"


def play_game():

    print("Welcome to Tic-Tac-Toe!")
    print("")
    project()
    print("")
    print("1. Play vs AI")
    print("2. Play vs Player")
    print("")

    mode = input("Choose mode (1 or 2): ")
    while mode not in ["1", "2"]:
        mode = input("Invalid choice. Please choose 1 or 2: ")
    
    if mode == "1":
        player_vs_ai()
    else:
        player_vs_player()

if __name__ == "__main__":
    play_game()


#Program By SAURABH JHA