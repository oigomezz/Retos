def solve(ans, l, r, m):
    count = 0
    for i in range(len(ans)):
        if ans[i] == l*m or ans[i] == r*m:
            count += 1
    return count


n, m, k = map(int, input().split())
ans = []
for i in range(n):
    a, b, c = map(int, input().split())
    temp = m*a+m*b-m*c
    ans.append(temp)

for i in range(m):
    l, r = map(int, input().split())
    print(solve(ans, l, r, m), end=' ')
