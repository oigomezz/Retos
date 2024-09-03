T = int(input())
for _ in range(T):
    n = int(input())
    alist = list(map(int, input().split()))
    AND = -1
    OR = 0
    for i in alist:
        OR |= i
        AND &= i
    OR = bin(OR).replace('0b', '').count('1')
    AND = bin(AND).replace('0b', '').count('1')
    res = 1 << (OR - AND)
    print(res)
