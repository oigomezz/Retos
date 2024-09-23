d = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}

n = input()
for i in n:
    d[i] += 1

for idx in range(10):
    print(idx, d[str(idx)])
