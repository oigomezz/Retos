T = int(input())
for i in range(T):
    N, A, B = [int(x) for x in input().split()]
    s = input()
    count = 0
    l = ""

    for i in range(N):
        if i < A:
            if s[i] != "0":
                l += "0"
                count += 1
            else:
                l = "0"
        elif i <= B:
            if s[i] != "0":
                l += "1"
                count += 1
            else:
                l += "1"
        else:
            l += "2"

    print(count)
    print(l)
