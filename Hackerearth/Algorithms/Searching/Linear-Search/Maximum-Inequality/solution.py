t = int(input())
for _ in range(t):
    n = int(input())
    a = input().rstrip()
    lva = lvb = ""
    cta = ctb = -1
    for v in a:
        if v != lva:
            cta += 1
            lva = v
        elif v != lvb:
            ctb += 1
            lvb = v
    print(cta + (ctb if ~ctb else 0))
