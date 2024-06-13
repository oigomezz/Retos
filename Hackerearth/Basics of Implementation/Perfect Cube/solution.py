n = int(input())
arr = list(map(int, input().split()))
ans = 0

for i in range(n):
    prod = 1
    for j in range(i, n):
        prod = prod * arr[j]
        cube_root = round(pow(prod, 1 / 3))
        if (cube_root * cube_root * cube_root == prod):
            ans += 1

print(ans)
