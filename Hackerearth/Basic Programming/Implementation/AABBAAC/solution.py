lengths = [0] * 1000
strings = [""] * 1000
tests = int(input())
for _ in range(tests):
    n, m = map(int, input().split())
    for i in range(1, n + 1):
        strings[i] = input().strip()

    for i in range(1, n + 1):
        lengths[i] = lengths[i - 1] * 2 + len(strings[i])

    for _ in range(m):
        x = int(input())
        for i in range(n, 0, -1):
            if x >= 2 * lengths[i - 1]:
                print(strings[i][x - 2 * lengths[i - 1]], end='')
                break
            elif x >= lengths[i - 1]:
                x = 2 * lengths[i - 1] - x - 1
    print()