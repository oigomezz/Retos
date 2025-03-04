parent = {}
size = {}


def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]


def union(i, j):
    a = find(i)
    b = find(j)
    if a is not b:
        if size[a] < size[b]:
            parent[a] = parent[b]
            size[b] += size[a]
        else:
            parent[b] = parent[a]
            size[a] += size[b]


if __name__ == "__main__":
    n, m = map(int, input().split())
    for i in range(n):
        parent[i] = i
        size[i] = 1
    for _ in range(m):
        u, v = map(int, input().split())
        union(u-1, v-1)
    for i in range(n):
        j = find(i)
        print(size[j]-1, end=" ")
    print()
