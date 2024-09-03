N = int(input())
li = [int(x) for x in input().split()]

count = 0
di = {}

for i in range(N):
    count += di.get(li[i] - i, 0)
    di[li[i] - i] = di.get(li[i] - i, 0) + 1

print(count * 2)
