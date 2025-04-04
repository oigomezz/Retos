t = int(input())
for _ in range(t):
    s, k = input().strip().split()
    k = int(k)
    idxes = list(range(len(s)))
    idxes.sort(key=lambda i, s=s: s[i], reverse=True)
    idx = idxes[k - 1]
    word = ''
    for _ in range(len(s)):
        word += s[idx]
        idx = idxes[idx]
    word = word[-1] + word[:-1]
    print(word)
