def minimax(board, depth, alpha, beta, maximizing_player):
    """
    Minimax algorithm with alpha-beta pruning to determine the best move for the current player.
    """
    if depth == 0 or board._check_if_game_end(board.board):
        if maximizing_player:
            return None, score_position(board.board, RED)
        else:
            return None, score_position(board.board, BLUE)

    if maximizing_player:
        max_score = float("-inf")
        best_column = None

        for column in range(7):
            if board.board[0][column] == EMPTY:
                board_copy = copy.deepcopy(board)
                board_copy.select_column(column)
                _, score = minimax(board_copy, depth - 1, alpha, beta, False)

                if score > max_score:
                    max_score = score
                    best_column = column

                alpha = max(alpha, max_score)
                if beta <= alpha:
                    break

        return best_column, max_score
    else:
        min_score = float("inf")
        best_column = None

        for column in range(7):
            if board.board[0][column] == EMPTY:
                board_copy = copy.deepcopy(board)
                board_copy.select_column(column)
                _, score = minimax(board_copy, depth - 1, alpha, beta, True)

                if score < min_score:
                    min_score = score
                    best_column = column

                beta = min(beta, min_score)
                if beta <= alpha:
                    break

        return best_column, min_score


def main():
    GameGUI()
    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)

        if not game_end:
            column, _ = minimax(board, depth=4, alpha=float("-inf"), beta=float("inf"), maximizing_player=True)
            board.select_column(column)

        time.sleep(2)


if __name__ == "__main__":
    main()