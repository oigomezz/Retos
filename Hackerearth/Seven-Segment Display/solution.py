d = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

t = int(input())

for _ in range(t):
    n = input().strip()
    matchsticks = 0
    for i in n:
        matchsticks += d[i]

    # Case 1 Max number when the number of Matchstick is even
    if matchsticks % 2 == 0:
        x = int(matchsticks/2)
        number = ''
        for j in range(x):
            number = number + '1'
    else:
        x = int((matchsticks-3)/2)
        number = '7'
        for j in range(x):
            number = number + '1'

    print(number)
