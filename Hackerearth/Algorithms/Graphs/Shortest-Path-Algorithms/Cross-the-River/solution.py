from collections import deque


def intersect(x1, y1, r1, x2, y2, r2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2


LIMIT = 1000000005
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        pt = []

        for i in range(n):
            x, y, r = map(int, input().split())
            pt.append(((x, y), r))

        A, B = map(int, input().split())

        q = deque()
        dis = [LIMIT] * n

        for i in range(n):
            if abs(pt[i][0][1] - B) <= pt[i][1]:
                dis[i] = 1
                q.append((1, i))

        while q:
            p = q.popleft()
            i = p[1]
            for j in range(n):
                if intersect(pt[i][0][0], pt[i][0][1], pt[i][1], pt[j][0][0], pt[j][0][1], pt[j][1]):
                    if dis[j] == LIMIT:
                        dis[j] = dis[i] + 1
                        q.append((dis[j], j))

        ans = LIMIT
        for i in range(n):
            if abs(pt[i][0][1] - A) <= pt[i][1]:
                ans = min(ans, dis[i])

        print(-1 if ans == LIMIT else ans)
