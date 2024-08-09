t = int(input())
for _ in range(t):
    bt1, bt2, mt1, mt2 = map(int, input().split())
    count = 0
    for i in range(min(bt1, bt2), max(bt1, bt2)+1):
        for j in range(min(mt1, mt2), max(mt1, mt2)+1):
            if (i == j):
                count += 1

    if count == 0:
        print("Line")
    elif count == 1:
        print("Point")
    else:
        print("Nothing")
