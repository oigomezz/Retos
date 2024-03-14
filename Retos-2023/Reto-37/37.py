class KindArmy:

    HARFOOT = 1
    SOUTHERNER = 2
    DWARF = 3
    NUMENOREAN = 4
    ELF = 5


class EvilArmy:

    SOUTHERNER = 2
    ORC = 2
    GOBLIN = 2
    WARG = 3
    TROLL = 5


def battle_for_the_middle_earth(kind_army, evil_army):
    kind_army_points = 0
    evil_army_points = 0

    for army in kind_army:
        kind_army_points += army[0] * army[1]

    for army in evil_army:
        evil_army_points += army[0] * army[1]

    if kind_army_points > evil_army_points:
        print("Gana el bien")
    elif evil_army_points > kind_army_points:
        print("Gana el mal")
    else:
        print("Empate")


battle_for_the_middle_earth(
    [
        (KindArmy.ELF, 1),
    ],
    [
        (EvilArmy.TROLL, 1),
    ],
)

battle_for_the_middle_earth(
    [
        (KindArmy.ELF, 1),
        (KindArmy.HARFOOT, 1),
    ],
    [
        (EvilArmy.TROLL, 1),
    ],
)

battle_for_the_middle_earth(
    [
        (KindArmy.ELF, 1),
        (KindArmy.HARFOOT, 1),
    ],
    [
        (EvilArmy.TROLL, 1),
        (EvilArmy.ORC, 1),
    ],
)

battle_for_the_middle_earth(
    [
        (KindArmy.ELF, 56),
        (KindArmy.HARFOOT, 80),
        (KindArmy.DWARF, 5),
    ],
    [
        (EvilArmy.TROLL, 17),
        (EvilArmy.ORC, 51),
        (EvilArmy.WARG, 10),
        (EvilArmy.SOUTHERNER, 2),
    ],
)
