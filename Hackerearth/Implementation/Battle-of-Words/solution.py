from collections import defaultdict

s1, s2 = "", ""


def solve():
    global s1, s2
    s1 = input()
    s2 = input()
    m1, m2 = defaultdict(int), defaultdict(int)

    for ch in s1:
        if ch != ' ':
            m1[ch] += 1

    for ch in s2:
        if ch != ' ':
            m2[ch] += 1

    for ch in s2:
        if ch != ' ':
            m1[ch] -= 1

    for ch in s1:
        if ch != ' ':
            m2[ch] -= 1

    ans, ans2 = "", ""

    for i in m1:
        if m1[i] > 0:
            ans += i

    for i in m2:
        if m2[i] > 0:
            ans2 += i

    if len(ans) != 0 and len(ans2) == 0:
        print("You win some.")
    elif len(ans) != 0 and len(ans2) != 0:
        print("You draw some.")
    else:
        print("You lose some.")

    s1, s2 = "", ""


t = int(input())
for _ in range(t):
    solve()
