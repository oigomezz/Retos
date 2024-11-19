t = int(input())
for _ in range(t):
    m = int(input())
    change_list = {}
    cost = 0
    for _ in range(m):
        a, b = input().strip().split()
        if a != b:
            cost += 1
            change_list[a] = b
    checked = set()
    for a in change_list:
        if a not in checked:
            checked.add(a)
            b = change_list[a]
            while True:
                if b == a:
                    cost += 1
                    break
                checked.add(b)
                if b not in change_list:
                    break
                b = change_list[b]
    print(cost)
