s = input()
DIFF = 1000000000000000000
length = len(s)
if length > 1:
    x = 10 ** (length - 1) - 1
    DIFF = int(s) - x
for i in range(length):
    d = int(s[i])
    if d % 2 == 0:
        a = s[:i] + (str(d - 1) if d != 0 else '9') + \
            '9' * (len(s) - i - 1)
        b = s[:i] + str(d + 1) + '1' * (len(s) - i - 1)
        d_a = abs(int(a) - int(s))
        d_b = abs(int(b) - int(s))
        if min(d_a, d_b) >= DIFF:
            s = '9' * (len(s) - 1)
        else:
            s = b if d_b < d_a else a
        break
print(s)
