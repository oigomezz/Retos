from enum import Enum
from typing import List


class TicTacToeValue(Enum):
    # trunk-ignore(ruff/E741)
    O = "O"
    X = "X"
    EMPTY = "EMPTY"


class TicTacToeResult(Enum):
    # trunk-ignore(ruff/E741)
    O = "O"
    X = "X"
    DRAW = "DRAW"
    NULL = "NULL"


def check_tic_tac_toe(board: List[List[TicTacToeValue]]) -> TicTacToeResult:

    # Null
    if len(board) != 3:
        return TicTacToeResult.NULL

    x_count = 0
    o_count = 0

    flat_board = []
    for row in board:
        flat_board += row

        if len(row) != 3:
            return TicTacToeResult.NULL

        for col in row:
            if col == TicTacToeValue.X:
                x_count += 1
            elif col == TicTacToeValue.O:
                o_count += 1

    if abs(x_count - o_count) > 1:
        return TicTacToeResult.NULL

    # Win or Draw
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    result = TicTacToeResult.DRAW

    for win_combination in win_combinations:

        if (
            flat_board[win_combination[0]] != TicTacToeValue.EMPTY
            and flat_board[win_combination[0]] == flat_board[win_combination[1]]
            and flat_board[win_combination[0]] == flat_board[win_combination[2]]
        ):

            winner = flat_board[win_combination[0]]

            if (
                result != TicTacToeResult.DRAW
                and (
                    TicTacToeValue.O
                    if result == TicTacToeResult.O
                    else TicTacToeValue.X
                )
                != winner
            ):
                return TicTacToeResult.NULL

            result = (
                TicTacToeResult.X if winner == TicTacToeValue.X else TicTacToeResult.O
            )

    return result


print(
    check_tic_tac_toe(
        [
            [TicTacToeValue.X, TicTacToeValue.O, TicTacToeValue.X],
            [TicTacToeValue.O, TicTacToeValue.X, TicTacToeValue.O],
            [TicTacToeValue.O, TicTacToeValue.O, TicTacToeValue.X],
        ]
    ).value
)

print(
    check_tic_tac_toe(
        [
            [TicTacToeValue.EMPTY, TicTacToeValue.O, TicTacToeValue.X],
            [TicTacToeValue.EMPTY, TicTacToeValue.X, TicTacToeValue.O],
            [TicTacToeValue.EMPTY, TicTacToeValue.O, TicTacToeValue.X],
        ]
    ).value
)

print(
    check_tic_tac_toe(
        [
            [TicTacToeValue.O, TicTacToeValue.O, TicTacToeValue.O],
            [TicTacToeValue.O, TicTacToeValue.X, TicTacToeValue.X],
            [TicTacToeValue.O, TicTacToeValue.X, TicTacToeValue.X],
        ]
    ).value
)

print(
    check_tic_tac_toe(
        [
            [TicTacToeValue.X, TicTacToeValue.O, TicTacToeValue.X],
            [TicTacToeValue.X, TicTacToeValue.X, TicTacToeValue.O],
            [TicTacToeValue.X, TicTacToeValue.X, TicTacToeValue.X],
        ]
    ).value
)
