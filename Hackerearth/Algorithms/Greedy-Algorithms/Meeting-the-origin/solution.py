t = int(input())
for _ in range(t):
    s = input()
    l_count = s.count('L')
    r_count = s.count('R')
    u_count = s.count('U')
    d_count = s.count('D')
    a = sum(divmod(abs(l_count - r_count), 2))
    b = sum(divmod(abs(u_count - d_count), 2))
    print(a + b)
