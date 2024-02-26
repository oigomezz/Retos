from enum import Enum

class Player(Enum):
    P1 = 1
    P2 = 2

def tennis_game(points: list):

    scores = {0: "Love", 1: "15", 2: "30", 3: "40"}
    p1_points = 0
    p2_points = 0

    for point in points:
        if point == "P1":
            p1_points += 1
        elif point == "P2":
            p2_points += 1
        
        if p1_points < 4 and p2_points < 4:
            print(scores[p1_points] + " - " + scores[p2_points])
        elif p1_points == p2_points:
            print("Deuce")
        elif p1_points > p2_points:
            if p1_points - p2_points == 1:
                print("Ventaja P1")
            else:
                print("Ha ganado el P1")
                return
        else:
            if p2_points - p1_points == 1:
                print("Ventaja P2")
            else:
                print("Ha ganado el P2")
                return

points = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
tennis_game(points)
