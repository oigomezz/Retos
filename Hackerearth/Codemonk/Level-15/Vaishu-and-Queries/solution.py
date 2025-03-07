from collections import defaultdict
balls = defaultdict(list)
dp = defaultdict(list)


def calculate(i, r, b, n):
    answer = 0
    if i == n:
        return 0

    str_d = (i, r, b)
    if dp.get(str_d) != None:
        return dp.get(str_d)

    ball_val = balls.get(i)
    r_val = ball_val.count("R")
    b_val = ball_val.count("B")

    ans1 = 0
    if r-r_val >= 0 and b-b_val >= 0:
        ans1 = calculate(i+1, r-r_val, b-b_val, n)+1

    ans2 = calculate(i+1, r, b, n)
    answer = max(ans1, ans2)
    dp[str_d] = answer

    return answer


pat = int(input())
for _ in range(pat):
    balls[_] = list(input())

query = int(input())
for _ in range(query):
    rb = list(map(int, input().split()))
    r = rb[0]
    b = rb[1]

    print(calculate(0, r, b, pat))
