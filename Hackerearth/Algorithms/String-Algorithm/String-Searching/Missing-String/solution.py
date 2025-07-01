from itertools import product
from string import ascii_lowercase

s = input().strip()
x = 1
while True:
    for p in product(ascii_lowercase, repeat=x):
        res = ''.join(p)
        if res not in s:
            print(res)
            break
    else:
        x += 1
        continue
    break
