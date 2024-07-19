t = int(input())
while t > 0:
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    if (x1-x2 == 0 and y1-y2 == 0) or (x3-x4 == 0 and y3-y4 == 0):
        print("INVALID")
    elif (y1-y2 == 0 and y3-y4 == 0 and x1-x2 != 0 and x3-x4 != 0) or (x1-x2 == 0 and x3-x4 == 0 and y1-y2 != 0 and y3-y4 != 0):
        print("NO")
    elif (x1-x2 == 0 and x3-x4 != 0 and y3-y4 != 0) or (x3-x4 == 0 and x1-x2 != 0 and y1-y2 != 0) or (y1-y2 == 0 and x3-x4 != 0 and y3-y4 != 0) or (y3 - y4 == 0 and x1-x2 != 0 and y1-y2 != 0):
        print("NO")
    elif (x1-x2 == 0 and y3-y4 == 0) or (y1-y2 == 0 and x3-x4 == 0):
        print("YES")
    elif round((y2-y1)/(x2-x1), 5) == round((-1/((y4-y3)/(x4-x3))), 5):
        print("YES")
    else:
        print("NO")
    t -= 1
