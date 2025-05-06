n, m = map(int, input().strip().split())
c = list(map(int, input().strip().split()))
numbers = list(map(lambda x: int(x) - 1, input().strip().split()))
assert len(c) == m
assert len(numbers) == n
last = 0
for i in range(n):
    last = (last // c[numbers[i]] + 1) * c[numbers[i]]
    while True:
        for j in range(numbers[i] + 1, m):
            if last % c[j] == 0:
                break
        else:
            break
        last += c[numbers[i]]
print(last)
