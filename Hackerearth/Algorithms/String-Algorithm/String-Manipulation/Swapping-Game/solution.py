k = int(input())
s = input()
n = len(s)
x = s
i = 0
while k:
    if n % 2:
        x = x[::2] + x[-2::-2]
    else:
        x = x[::2] + x[::-2]
    k -= 1
    i += 1
    if s == x:
        k %= i
print(x)
