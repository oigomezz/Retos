T = int(input())
for _ in range(T):
    s = input()
    count = 0
    for i in range(len(s) // 2):
        if s[i] == '(':
            count += 1
    print(2 * count)
