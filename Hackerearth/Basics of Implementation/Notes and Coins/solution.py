import math

n = int(input())
map = {}

for _ in range(n):
    s, r = input().split()
    r = int(r)
    if s not in map:
        map[s] = []
    map[s].append(r)

coin = True
note = True

for key, values in map.items():
    if key == "Coin":
        if coin:
            print("Coins :")
            coin = False
        for value in values:
            print(value)
    elif key == "Note":
        if note:
            print("Notes :")
            note = False
        for value in values:
            print(value)
