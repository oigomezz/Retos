x = ['0', '1', '8']
t = int(int(input()))
for _ in range(t):
    n = int(input())
    if str(n) == str(n)[::-1] and set(str(n)).issubset(x):
        print('YES')
    else:
        print('NO')
