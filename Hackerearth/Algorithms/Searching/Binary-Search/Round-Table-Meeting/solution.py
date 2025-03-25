from bisect import bisect_left, bisect_right


nums, numq = map(int, input().split())
student = list(map(int, input().split()))
p = {}
for i in range(len(student)):
    n = p.get(student[i], [])
    n.append(i)
    p[student[i]] = n
for i in range(numq):
    a, b = map(int, input().split())
    if a == b:
        print(0)
        continue
    p1, p2 = p[a], p[b]
    if len(p1) > len(p2):
        p1, p2 = p2, p1
    l = float('inf')
    for pos in p1:
        lo, hi = bisect_left(p2, pos)-1, bisect_right(p2, pos)
        distl = (pos-p2[lo]) % nums
        distr = (p2[hi % len(p2)]-pos) % nums
        l = min(l, distl, distr)
    print(l//2)
