t = int(input())
while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    ans = 0
    carry = 0
    for num in arr:
        ans += (num+carry) % 2
        carry = (num+carry)//2
    while carry:
        ans += carry % 2
        carry = carry//2
    print(ans)
    t -= 1
