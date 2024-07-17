def is_name(name):
    flag = 0
    for digit in name:
        if digit.isalpha():
            flag = 1
            break
    return flag


t = int(input())
while t > 0:
    arr = input().split()
    fg = 0
    if len(arr) == 3:
        x, y, z = arr[0], arr[1], arr[2]
        if (x.isdigit() and x[0] != '0' and y.isdigit() and y[0] != '0' and is_name(z)) or (x.isdigit() and x[0] != '0' and z.isdigit() and z[0] != '0' and is_name(y)) or (y.isdigit() and y[0] != '0' and z.isdigit() and z[0] != '0' and is_name(x)):
            fg = 1
    elif len(arr) == 2:
        x, y = arr[0], arr[1]
        if (x.isdigit() and x[0] != '0' and not y.isdigit()) or (y.isdigit() and y[0] != '0' and not x.isdigit()):
            fg = 2

    if fg == 1:
        print('V')
    elif fg == 2:
        print('M')
    else:
        print('N')

    t -= 1
