n = int(input())
s = input()
t = input()

days = 0
for i, j in zip(s, t):
    ord_i = ord(i)
    ord_j = ord(j)
    k = (ord_j - ord_i) % 26
    days += k // 13
    days += k % 13

print(days)
