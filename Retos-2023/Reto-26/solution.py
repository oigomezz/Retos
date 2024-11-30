from typing import List, Tuple


class Move:
    ROCK = "ROCK"
    SCISSORS = "SCISSORS"
    PAPER = "PAPER"


def rock_scissors_paper(games: List[Tuple[Move, Move]]) -> str:
    player_one_games = 0
    player_two_games = 0

    for game in games:
        player_one_move = game[0]
        player_two_move = game[1]

        if player_one_move != player_two_move:
            if (
                player_one_move == Move.ROCK
                and player_two_move == Move.SCISSORS
                or player_one_move == Move.SCISSORS
                and player_two_move == Move.PAPER
                or player_one_move == Move.PAPER
                and player_two_move == Move.ROCK
            ):

                player_one_games += 1
            else:
                player_two_games += 1

    if player_one_games == player_two_games:
        return "Tie"
    elif player_one_games > player_two_games:
        return "Player 1"
    else:
        return "Player 2"


print(rock_scissors_paper([(Move.ROCK, Move.ROCK)]))
print(rock_scissors_paper([(Move.ROCK, Move.SCISSORS)]))
print(rock_scissors_paper([(Move.PAPER, Move.SCISSORS)]))
print(
    rock_scissors_paper(
        [
            (Move.ROCK, Move.ROCK),
            (Move.SCISSORS, Move.SCISSORS),
            (Move.PAPER, Move.PAPER),
        ]
    )
)
print(
    rock_scissors_paper(
        [
            (Move.ROCK, Move.SCISSORS),
            (Move.SCISSORS, Move.PAPER),
            (Move.SCISSORS, Move.ROCK),
        ]
    )
)
print(
    rock_scissors_paper(
        [
            (Move.ROCK, Move.PAPER),
            (Move.SCISSORS, Move.ROCK),
            (Move.PAPER, Move.SCISSORS),
        ]
    )
)
