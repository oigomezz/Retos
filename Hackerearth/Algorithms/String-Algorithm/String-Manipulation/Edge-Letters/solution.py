s = [el for el in input()]
ans = [[0]*(26) for _ in range(26)]
freq = [0]*(26)
for i in range(len(s)):
    c = ord(s[i])-ord("a")
    freq[c] += 1
    for j in range(26):
        ans[j][c] += freq[j]
for _ in range(int(input())):
    t = [el for el in input().split()]
    i = ord(t[0])-ord("a")
    j = ord(t[1])-ord("a")
    print(ans[i][j])
