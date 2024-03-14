class PokemonType:
    def __init__(self, name):
        self.name = name


WATER = PokemonType("Agua")
FIRE = PokemonType("Fuego")
GRASS = PokemonType("Planta")
ELECTRIC = PokemonType("Eléctrico")


class PokemonChart:
    def __init__(self, effective, not_effective):
        self.effective = effective
        self.not_effective = not_effective


def battle(attacker, defender, attack, defense):
    if attack <= 0 or attack > 100 or defense <= 0 or defense > 100:
        print("El ataque o la defensa contiene un valor incorrecto")
        return None

    type_chart = {
        WATER: PokemonChart(FIRE, GRASS),
        FIRE: PokemonChart(GRASS, WATER),
        GRASS: PokemonChart(WATER, FIRE),
        ELECTRIC: PokemonChart(WATER, GRASS),
    }

    effectivity = 1.0
    if attacker == defender or type_chart[attacker].not_effective == defender:
        effectivity = 0.5
        print("No es muy efectivo")
    elif type_chart[attacker].effective == defender:
        effectivity = 2.0
        print("Es súper efectivo")
    else:
        print("Es neutro")

    return 50 * attack / defense * effectivity


print(battle(WATER, FIRE, 50, 30))
print(battle(WATER, FIRE, 101, -10))
print(battle(FIRE, WATER, 50, 30))
print(battle(FIRE, FIRE, 50, 30))
print(battle(GRASS, ELECTRIC, 30, 50))
