from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = Counter(input().split())
    if len(a) > 2 * k:
        print("NO")
    elif len(a) == 2 * k:
        print("YES")
    else:
        ans = "NO"
        c = len(a)
        for x in sorted(a.values(), reverse=1):
            if x > 1:
                c += 1
            else:
                break
            if c == 2 * k:
                ans = "YES"
                break
        print(ans)
