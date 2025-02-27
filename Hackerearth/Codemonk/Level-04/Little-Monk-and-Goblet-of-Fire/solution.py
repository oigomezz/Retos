from collections import deque

q = int(input())
que = [deque() for _ in range(5)]
que1 = deque()

for _ in range(q):
    line = list(input().split())
    if line[0] == 'E':
        a, b = map(int, line[1:])
        if not que[a]:
            que1.append(a)
        que[a].append(b)
    else:
        temp = que1.popleft()
        print(temp, que[temp].popleft())
        que[temp].pop()
        if not que[temp]:
            que1.pop()
