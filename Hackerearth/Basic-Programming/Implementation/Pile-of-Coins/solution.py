t = int(input())
for _ in range(t):
    p, q = list(map(int, input().split()))
    if (p % 2 == 0 or q % 2 == 0):
        print("Ashish")
    else:
        print("Jeel")
