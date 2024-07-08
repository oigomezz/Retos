T = int(input())

for _ in range(T):
    l = list(map(int, input().split()))
    print(max(l)//min(l))
