count = [0] * 201
xor_result = 0
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    x = arr[i]
    count[x] += 1
    xor_result ^= x

current = {0: 0}
for a in range(1, 201):
    if count[a] == 0:
        continue
    previous = current.copy()

    for key, value in previous.items():
        x = key ^ a
        if x in current:
            current[x] = min(current[x], value + 1)
        else:
            current[x] = value + 1

q = int(input())
for _ in range(q):
    x = int(input())
    x ^= xor_result
    print(current[x] if x in current else -1)
