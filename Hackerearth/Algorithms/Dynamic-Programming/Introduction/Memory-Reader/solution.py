from sys import setrecursionlimit

setrecursionlimit(1000)


def read(point, start, end, arr):
    if start == end:
        return True
    if start in arr:
        for move in filter(lambda x: x > 0, (point - 1, point, point + 1)):
            new_start = start + move
            if new_start in memory and read(move, new_start, end, arr):
                return True
    return False


t = int(input())
for _ in range(t):
    n = int(input())
    memory = list(map(int, input().strip().split()))
    if read(memory[0], memory[0], memory[-1], set(memory)):
        print('YES')
    else:
        print('NO')
