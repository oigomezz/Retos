from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)


def dfs(vertex):
    global total, visited, on_stack, answer
    visited[vertex] = on_stack[vertex] = True
    for adjacent in graph[vertex]:
        if visited[adjacent]:
            if not on_stack[adjacent]:
                answer = False
            else:
                total[adjacent] -= 1
                total[vertex] += 1
        else:
            dfs(adjacent)
            total[vertex] += total[adjacent]
    if vertex != 1 and total[vertex] != 1:
        answer = False
    on_stack[vertex] = False


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n, m = map(int, input().split())
        graph = defaultdict(list)

        for __ in range(m):
            u, v = map(int, input().split())
            if u != v:
                graph[u].append(v)

        visited = [False] * (n + 1)
        total = [0] * (n + 1)
        on_stack = [False] * (n + 1)
        answer = True

        dfs(1)

        count = sum(visited[1:n + 1])
        if count != n:
            answer = False

        if answer:
            print("Yes")
        else:
            print("No")
