t = int(input())
for _ in range(t):
    n = int(input())
    same = [0, 0]
    for i in range(n):
        s = input()
        if s.find('0') == -1:
            same[1] += 1
        elif s.find('1') == -1:
            same[0] += 1
    print(n * (n - 1) // 2 - same[0] * same[1])
