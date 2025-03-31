from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

count_map = defaultdict(int)
for num in arr:
    count_map[num] += 1

total_pairs = 0
for count in count_map.values():
    if count > 1:
        total_pairs += count * (count - 1) // 2

print(total_pairs)
