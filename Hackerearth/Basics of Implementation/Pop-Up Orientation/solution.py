t = int(input())
while t > 0:
    x, y, l, m, a, b = map(int, input().split())
    if a + l <= x and b - m >= 0:
        print("bottom-right")
    elif a - l >= 0 and b - m >= 0:
        print("bottom-left")
    elif a + l <= x and b + m <= y:
        print("top-right")
    else:
        print("top-left")
    t -= 1
