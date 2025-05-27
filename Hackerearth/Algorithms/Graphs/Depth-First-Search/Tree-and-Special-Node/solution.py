from collections import defaultdict

cnt = 0
N = int(1e6 + 2)
arr = [0] * N
graph = defaultdict(list)
visited = [0] * N


def recursive_function(index):
    global cnt
    visited[arr[index]] = 1
    cnt += 1
    for neighbor in graph[index]:
        if not visited[arr[neighbor]]:
            recursive_function(neighbor)
    visited[arr[index]] = 0


if __name__ == "__main__":
    n = int(input().strip())
    arr[1:n + 1] = list(map(int, input().strip().split()))
    for _ in range(1, n):
        x, y = map(int, input().strip().split())
        graph[x].append(y)
        graph[y].append(x)

    recursive_function(1)
    print(" ".join(map(str, [cnt])))
