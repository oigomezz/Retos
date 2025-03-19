t = int(input())
for _ in range(t):
    n = int(input())
    need = {}
    for i in range(n):
        [l, r, z] = map(int, input().split())
        if r not in need:
            need[r] = 0
        need[r] += z
    ans = 0
    li = list(need.items())
    li.sort()
    cur_need = 0
    for key, val in li:
        cur_need += val
        ans = max(ans, (cur_need + key - 1) // key)
    print(ans)
