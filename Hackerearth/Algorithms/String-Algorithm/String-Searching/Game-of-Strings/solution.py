def preprocess(pat):
    n = len(pat)
    lps = [0] * n
    i = 1
    j = 0
    while i < n:
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


t = int(input())
for _ in range(t):
    s, k = map(str, input().strip().split())
    k = int(k)
    kmp = preprocess(s)
    mx = max(kmp[:k])
    res = None
    x = kmp[-1]
    while x > 0:
        if x <= mx:
            res = x
            break
        x = kmp[x - 1]
    if not res:
        print("Puchi is a cheat!")
    else:
        print(s[:res])
