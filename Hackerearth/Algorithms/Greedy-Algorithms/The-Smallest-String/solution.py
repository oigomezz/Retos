t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    s = input()
    list_s = list(s)
    ord_z = ord('z')
    for i in range(n):
        ord_c = ord(list_s[i])
        if list_s[i] != 'a' and ord_z - ord_c + 1 <= k:
            list_s[i] = 'a'
            k -= ord_z - ord_c + 1
        if k == 0:
            break
    k %= 26
    list_s[-1] = chr(ord(list_s[-1]) + k)
    print(*list_s, sep='')
