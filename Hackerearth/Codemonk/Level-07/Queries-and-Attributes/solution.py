from collections import defaultdict


num = int(input())
arr = [int(x) for x in input().split()]
lefts = [0] * num
rights = [0] * num
b = [0] * num
multiset = set()
additions = defaultdict(list)
removals = defaultdict(list)

for i in range(num):
    line = list(map(int, input().split()))
    lefts[i] = int(line[0]) - 1
    rights[i] = int(line[1]) - 1

for i in range(num - 1, -1, -1):
    for x in additions[i]:
        multiset.add(x)
    if i != num - 1:
        b[i] = min(multiset) if multiset else 1000000000000000000
    if i > 0:
        additions[rights[i]].append(b[i] + arr[i])
        removals[lefts[i]].append(b[i] + arr[i])
    for x in removals[i]:
        multiset.discard(x)

for i in range(1, num):
    b[i] = min(b[i - 1], b[i])

q = int(input())
for _ in range(q):
    line = list(map(int, input().split()))
    query_x = int(line[0]) - 1
    query_y = int(line[1])

    print(b[query_x] + query_y)
