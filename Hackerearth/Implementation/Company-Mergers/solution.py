from collections import Counter

import numpy as np


n = int(input())
m = int(input())

mar = []
for i in range(n):
    mar.append(input().split(' '))

mar = np.array(mar)
mar = mar.flatten()
mar = Counter(mar)
mar = list(mar.values())

M = max(mar)

if M > 2:
    C = mar.count(M)
    count = max(mar)-2
    if C > 1 and C != len(mar):
        count += 1
else:
    count = 0

print(count)
