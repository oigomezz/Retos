def rock_paper_scissor_lizard_spock(games):

    rules = {
        "🗿": ["✂️", "🦎"],
        "📄": ["🗿", "🖖"],
        "✂️": ["📄", "🦎"],
        "🦎": ["🖖", "📄"],
        "🖖": ["🗿", "✂️"],
    }

    player_one = 0
    player_two = 0

    for game in games:
        player_one_game = game[0]
        player_two_game = game[1]
        if player_one_game != player_two_game:
            if player_two_game in rules[player_one_game]:
                player_one += 1
            else:
                player_two += 1

    if player_one == player_two:
        return "Tie"
    elif player_one > player_two:
        return "Player 1"
    else:
        return "Player 2"


print(rock_paper_scissor_lizard_spock([("🗿", "🗿")]))
print(rock_paper_scissor_lizard_spock([("🗿", "✂️")]))
print(rock_paper_scissor_lizard_spock([("✂️", "🗿")]))
print(
    rock_paper_scissor_lizard_spock(
        [("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿")]
    )
)
print(
    rock_paper_scissor_lizard_spock(
        [("🖖", "🗿"), ("✂️", "📄"), ("🗿", "🗿"), ("🦎", "🖖")]
    )
)
