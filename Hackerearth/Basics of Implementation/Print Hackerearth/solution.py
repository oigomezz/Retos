n = int(input())
m = input()[:n]
a = m.count('h')//2
b = m.count('a')//2
c = m.count('c')
d = m.count('k')
e = m.count('e')//2
f = m.count('r')//2
j = m.count('t')

y = [a, b, c, d, e, f, j]
y.sort()

print(y[0])
