from collections import defaultdict

test_cases = int(input())
for _ in range(test_cases):
    s = input()
    q = int(input())
    for _ in range(q):
        qstr = input()
        a = defaultdict(int)
        b = defaultdict(int)
        for char in qstr:
            a[char] += 1

        j = -1
        x = 0
        ans = 0

        for i in range(len(s)):
            b[s[i]] += 1
            if b[s[i]] == a[s[i]]:
                x += 1
            if x == len(qstr):
                while True:
                    j += 1
                    b[s[j]] -= 1
                    ans += len(s) - i
                    if b[s[j]] < a[s[j]]:
                        x -= 1
                        break

        print(ans)
