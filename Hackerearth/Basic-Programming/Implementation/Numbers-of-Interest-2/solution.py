spf = [0] * 1000002
sum_divisors = [0] * 1000002

for i in range(2, 1000002):
    if spf[i] == 0:
        for j in range(i, 1000002, i):
            if spf[j] == 0:
                spf[j] = i

for i in range(1, 1000002):
    for m in range(i, 1000002, i):
        sum_divisors[m] += i

for i in range(1, 1000002):
    sum_divisors[i] -= i
    sum_divisors[i] += sum_divisors[i - 1]
    spf[i] += spf[i - 1]

t = int(input())
for _ in range(t):
    n = int(input())
    print((spf[n] + sum_divisors[n]) % n)
