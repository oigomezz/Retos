from collections import defaultdict

test_cases = int(input())
results = []

for _ in range(test_cases):
    n = int(input())
    s = list(input())
    mask = 0
    count = 0
    char_map = defaultdict(int)
    char_map[0] = 1

    for i in range(n):
        mask ^= (1 << (ord(s[i]) - ord('a')))
        count += char_map[mask]
        char_map[mask] += 1

    results.append(str(count))

print("\n".join(results))
