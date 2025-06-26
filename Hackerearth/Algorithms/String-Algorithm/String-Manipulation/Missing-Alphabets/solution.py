t = int(input())
for _ in range(t):
    e = input().strip()
    m = int(input())
    d = {v: i for i, v in enumerate(e)}
    s = []
    for _ in range(m):
        s.append(input().strip())
    s.sort(key=lambda x: [d[i] for i in x])
    print(*s, sep='\n')
