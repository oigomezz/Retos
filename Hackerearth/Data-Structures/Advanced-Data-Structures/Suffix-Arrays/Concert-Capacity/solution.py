def solution(n, c, audience):
    for i in range(n):
        total = 0
        for j in range(n):
            if audience[i][1] <= audience[j][1] <= audience[i][2]:
                total += audience[j][0]
        if total > c:
            return 'No'
    return 'Yes'


N = int(input())
C = int(input())
audience = [list(map(int, input().split())) for _ in range(N)]

out_ = solution(N, C, audience)
print(out_)
