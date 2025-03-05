a = int(input())
odd = even = 0
s = list(map(int, input().split(" ")))
k = s[::-1]
k.append(0)
s = k[::-1]
for i in range(1, a+1):
    s[i] += s[i-1]
    if (s[i] % 2):
        odd = odd+1
    else:
        even = even+1

count = (even*(even-1))//2 + even + (odd*(odd-1))//2
print(count)
