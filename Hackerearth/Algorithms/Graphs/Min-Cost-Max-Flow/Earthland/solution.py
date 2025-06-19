from collections import defaultdict


def matching(u, adj, assign, vis):
    for v in adj[u]:
        if vis[v]:
            continue
        vis[v] = True
        if assign[v] == 0 or matching(assign[v], adj, assign, vis):
            assign[v] = u
            return True
    return False


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n, m = map(int, input().split())
        adj = defaultdict(list)
        assign = [0] * (n + 1)

        for _ in range(m):
            u, v = map(int, input().split())
            adj[v].append(u)

        answer = -1
        for i in range(1, n + 1):
            vis = [False] * (n + 1)
            if not matching(i, adj, assign, vis):
                answer += 1

        print(answer)
