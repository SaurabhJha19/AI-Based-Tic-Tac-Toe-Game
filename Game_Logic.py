import math

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

#Program By SAURABH JHA