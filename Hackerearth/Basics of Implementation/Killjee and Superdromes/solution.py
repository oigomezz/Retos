def is_palindrome(num, base):
    s = []
    while num > 0:
        s.append(num % base)
        num //= base
    return s == s[::-1]


ar = [0] * 1000000
arcount = 0


def solve(n):
    global arcount
    if arcount < n:
        total = ar[arcount]
        for i in range(arcount + 1, n + 1, 2):
            if is_palindrome(i, 10) and is_palindrome(i, 2):
                total += 1
            arcount += 1
            ar[arcount] = total
            arcount += 1
            ar[arcount] = total
        return total
    else:
        return ar[n]


q = int(input())
n = list(map(int, input().split()))
for i in range(q):
    out_ = solve(n[i])
    print(out_)
    print('\n')
