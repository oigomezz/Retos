from collections import defaultdict

test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    s = input()
    count = defaultdict(int)
    for i in range(n):
        count[s[i]] += 1
    odd = 0
    for count in count.values():
        odd += (count % 2)
    print(max(0, odd - 1))
