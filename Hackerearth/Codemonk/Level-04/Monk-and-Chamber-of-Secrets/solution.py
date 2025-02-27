from collections import deque

n, x = map(int, input().split())
a = deque([(int(temp), i+1) for i, temp in enumerate(input().split())])
b = deque()

for _ in range(x):
    j = 0
    hold = (-1, 0)
    while a and j < x:
        b.append(a.popleft())
        if hold[0] < b[-1][0]:
            hold = b[-1]
        j += 1
    print(hold[1], end=" ")
    while b:
        temp = b.popleft()
        if temp != hold:
            if temp[0] > 0:
                temp = (temp[0]-1, temp[1])
            a.append(temp)
print()
