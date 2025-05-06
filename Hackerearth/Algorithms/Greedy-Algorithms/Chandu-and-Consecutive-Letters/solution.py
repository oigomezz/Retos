import re

t = int(input())
for _ in range(t):
    s = input().strip()
    r = re.sub(r'(.)\1+', r'\1', s)
    print(r)
