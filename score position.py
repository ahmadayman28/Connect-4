def score_position(board, player):
    """
    Calculate the score of the current board position for the given player.
    """
    score = 0

    # Score center column
    center_column = [board[i][3] for i in range(6)]
    center_count = center_column.count(player)
    score += center_count * 3

    # Score horizontal
    for row in range(6):
        row_window = board[row]
        for col in range(4):
            window = row_window[col:col + 4]
            score += evaluate_window(window, player)

    # Score vertical
    for col in range(7):
        col_window = [board[row][col] for row in range(6)]
        for row in range(3):
            window = col_window[row:row + 4]
            score += evaluate_window(window, player)

    # Score diagonal (/)
    for row in range(3):
        for col in range(4):
            window = [board[row + i][col + i] for i in range(4)]
            score += evaluate_window(window, player)

    # Score diagonal (\)
    for row in range(3):
        for col in range(4):
            window = [board[row + 3 - i][col + i] for i in range(4)]
            score += evaluate_window(window, player)

    return score