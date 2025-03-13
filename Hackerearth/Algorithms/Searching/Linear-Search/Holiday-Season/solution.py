n = int(input())
s = input()

freq = [0] * 26
aage = [0] * 26
peeche = [[0] * 26 for _ in range(26)]
for i in range(n):
    aage[ord(s[i]) - ord('a')] += 1

ans = 0

for i in range(n):
    aage[ord(s[i]) - ord('a')] -= 1
    for j in range(26):
        ans += peeche[j][ord(s[i]) - ord('a')] * aage[j]
    for j in range(26):
        peeche[ord(s[i]) - ord('a')][j] += freq[j]
    freq[ord(s[i]) - ord('a')] += 1

print(ans)
