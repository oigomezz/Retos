def solution(N, S, comments):
    S = S.lower()
    comments = [comment.lower() for comment in comments]
    c = 0
    for comment in comments:
        if S in comment:
            c += 1
    return c


N = int(input())
S = input()
comments = [input() for _ in range(N)]

out_ = solution(N, S, comments)
print(out_)
