from collections import deque

members = []
n, rc0 = map(int, input().strip().split())
for _ in range(n):
    idx, rc = map(int, input().split())
    members.append((idx, rc))

i = 0
queue = deque([(0, rc0, 0)])
while queue:
    parent, rc, lvl = queue.popleft()
    age = 1
    while rc and i < n:
        print(parent, lvl + 1, age)
        queue.append((members[i][0], members[i][1], lvl + 1))
        rc -= 1
        i += 1
        age += 1
