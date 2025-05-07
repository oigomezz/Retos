t = int(input())
for _ in range(t):
    n = int(input())
    b, g = map(int, input().strip().split())
    if abs(b - g) <= 1:
        print('The teacher wins!')
    else:
        print('Little Jhool wins!')