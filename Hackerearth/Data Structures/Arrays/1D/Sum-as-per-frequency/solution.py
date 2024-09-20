N = int(input())
xs = input()
xs = [int(x) for x in xs.split()]
Q = int(input())
qs = []
for i in range(Q):
    q = input()
    [l, r] = q.split()
    qs.append((int(l), int(r)))

nf = {}
for x in xs:
    f = nf.get(x, 0)
    nf[x] = f + 1

fn = {}
for k, v in nf.items():
    ns = fn.get(v, 0)
    fn[v] = ns + k*v

fs = []
for i in range(max(fn.keys()) + 1):
    fs.append(fn.get(i, 0))

for (l, r) in qs:
    print(sum(fs[l:r+1]))
