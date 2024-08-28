t = int(input())
for _ in range(t):
    s = 0
    date1, date2 = map(str, input().split())
    d1 = int(date1[:2])
    m1 = int(date1[3:5])
    y1 = int(date1[6:8])
    yy1 = int(date1[8:10])
    d2 = int(date2[:2])
    m2 = int(date2[3:5])
    y2 = int(date2[6:8])
    yy2 = int(date2[8:10])
    d = y2-y1
    if (yy1 < 3 and yy2 > 13):
        s += (11*(d+1))
    elif ((yy1 > 13 and yy2 > 13) or (yy1 < 3 and yy2 < 3)):
        s += (11*d)
    elif (yy1 > 13 and yy2 < 3):
        if d == 0:
            s += 0
        else:
            s += (11*(d-1))
    elif (yy1 > 13 and yy2 <= 13):
        if (d2+1 >= m2 and m2+1 >= yy2) or (m2+1 > yy2):
            if d == 0:
                s += (yy2-yy1)
            elif d == 1:
                s += (yy2-2)
            else:
                s += ((yy2-2)+(11*(d-1)))
        else:
            if d == 0:
                s += (yy2-yy1-1)
            elif d == 1:
                s += (yy2-3)
            else:
                s += ((yy2-3)+(11*(d-1)))
    elif (yy1 < 3 and yy2 <= 13):
        if (d2+1 >= m2 and m2+1 >= yy2) or (m2+1 > yy2):
            if d == 0:
                s += (yy2-2)
            elif d == 1:
                s += 11+(yy2-2)
            else:
                s += ((yy2-2)+(11*d))
        else:
            if d == 0:
                s += (yy2-3)
            elif d == 1:
                s += 11+(yy2-3)
            else:
                s += ((yy2-3)+(11*d))
    elif (yy1 <= 13 and yy2 < 3):
        if ((d1+1 <= m2 and m1+1 == yy1) or (m1+1 < yy1)):
            if d == 0:
                s += (yy2-yy1)
            elif d == 1:
                s += (14-yy1)
            else:
                s += ((14-yy1)+(11*(d-1)))
        else:
            if d == 0:
                s += (yy2-yy1-1)
            elif d == 1:
                s += (13-yy1)
            else:
                s += ((13-yy1)+(11*(d-1)))
    elif (yy1 <= 13 and yy2 > 13):
        if ((d1+1 <= m1 and m1+1 <= yy1) or (m1+1 < yy1)):
            if d == 0:
                s += (14-yy1)
            elif d == 1:
                s += (14-yy1)+11
            else:
                s += ((14-yy1)+(11*(d)))
        else:
            if d == 0:
                s += (13-yy1)
            elif d == 1:
                s += (13-yy1)+11
            else:
                s += ((13-yy1)+(11*(d)))
    else:
        if (((d1+1 <= m1 and m1+1 == yy1) or (m1+1 < yy1)) and ((d2+1 >= m2 and m2+1 >= yy2) or (m2+1 > yy2))):
            if d == 0:
                s += (yy2-yy1+1)
            elif d == 1:
                s += (14-yy1)+(yy2-2)
            else:
                s += ((14-yy1)+(yy2-2)+(11*(d-1)))
        elif ((d1+1 <= m1 and m1+1 == yy1) or (m1+1 < yy1)):
            if d == 0:
                s += (yy2-yy1)
            elif d == 1:
                s += ((14-yy1)+(yy2-3))
            else:
                s += ((14-yy1)+(yy2-3)+(11*(d-1)))
        elif ((d2+1 >= m2 and m2+1 >= yy2) or (m2+1 > yy2)):
            if d == 0:
                s += (yy2-yy1)
            elif d == 1:
                s += ((13-yy1)+(yy2-2))
            else:
                s += ((13-yy1)+(yy2-2)+(11*(d-1)))
        else:
            if d == 0:
                s += (yy2-yy1-1)
            elif d == 1:
                s += ((13-yy1)+(yy2-3))
            else:
                s += ((13-yy1)+(yy2-3)+(11*(d-1)))
    print(s)
