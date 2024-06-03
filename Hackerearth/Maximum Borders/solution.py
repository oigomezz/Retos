t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    max_border = 0
    for _ in range(n):
        row = input().strip()
        if not row:
            continue
        lst = list(row)
        count_hash = 0
        a = []
        for c in range(len(lst)):
            if lst[c] == '#':
                count_hash += 1
                a.append(count_hash)
            else:
                count_hash = 0
        if a:
            max_border = max(max_border, max(a))
    print(max_border)
