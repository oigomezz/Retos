def solution(n, c):
    stack = []
    for i in c:
        if i:
            stack.append(i)
        else:
            yield stack.pop()


N = int(input())
C = list(map(int, input().split()))

out_ = solution(N, C)
print(" ".join(map(str, out_)))
