t = int(input())
for _ in range(t):
    n, x, y = map(int, input().strip().split())
    stack_1 = []
    stack_2 = []
    for i in range(n):
        a, b = map(int, input().strip().split())
        stack_1.append(a)
        stack_2.append(b)

    effort = 0
    stack_1.sort()
    stack_2.sort()
    for i in range(n):
        if stack_1[i] > stack_2[i]:
            effort += y * (stack_1[i] - stack_2[i])
        else:
            effort += x * (stack_2[i] - stack_1[i])

    print(effort)
