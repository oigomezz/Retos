n = int(input())
ans = [0] * 100017
set_ans = set()

for i in range(1, n):
    ans[i] = i - n

a = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1
    if a[i] < n:
        ans[(a[i] - i + n) % n] += 1

for i in range(n):
    set_ans.add(ans[i])

q = int(input())
for _ in range(q):
    i, nw = map(int, input().split())
    i -= 1
    nw -= 1

    if a[i] < n:
        set_ans.remove(ans[(a[i] - i + n) % n])
        ans[(a[i] - i + n) % n] -= 1
        set_ans.add(ans[(a[i] - i + n) % n])

    a[i] = nw

    if a[i] < n:
        set_ans.remove(ans[(a[i] - i + n) % n])
        ans[(a[i] - i + n) % n] += 1
        set_ans.add(ans[(a[i] - i + n) % n])

    print(n - max(set_ans))
