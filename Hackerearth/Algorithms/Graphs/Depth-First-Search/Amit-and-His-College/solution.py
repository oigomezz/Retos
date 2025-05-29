t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    prerequisites = {}
    for _ in range(m):
        u, v = map(int, input().strip().split())
        prerequisites[u] = v
    for course in prerequisites:
        if prerequisites[course] in prerequisites and prerequisites[prerequisites[course]] == course:
            print(0)
            break
    else:
        print(1)
