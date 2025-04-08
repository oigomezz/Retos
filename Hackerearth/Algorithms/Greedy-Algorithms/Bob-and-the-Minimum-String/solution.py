from collections import Counter, deque

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    ans = ''
    chars = sorted(set(s))
    counter = Counter(s)
    i = 0
    end = len(chars) - 1
    stack = deque([])
    for c in s:
        counter[c] -= 1
        stack.append(c)
        while i < end and counter[chars[i]] <= 0:
            i += 1
        while stack and chars[i] >= stack[-1]:
            ans += stack.pop()
    print(ans)
