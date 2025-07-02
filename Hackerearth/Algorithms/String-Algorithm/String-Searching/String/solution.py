from collections import Counter

n = int(input())
s = input().strip()
print(n - Counter(s).most_common(1)[0][-1])
