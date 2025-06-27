T = int(input())
for tc in range(T):
    s = input().strip()
    v = [0] * 26
    for i in s:
        v[ord(i) - ord('a')] += 1
    c = sum(i // 2 for i in v)
    print(c)
