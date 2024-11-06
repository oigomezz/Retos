from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

g = defaultdict(list)
custo = [0] * 100005
in_time = [0] * 100005
out_time = [0] * 100005
tour = [0] * 100005
tempo = 1
blacklist = [-1] * 100005
bit = [0] * 100005


def dfs(node, p=-1):
    global tempo
    global tour
    tour[tempo] = node
    in_time[node] = tempo
    tempo += 1
    for to in g[node]:
        if to != p:
            dfs(to, node)
    out_time[node] = tempo - 1


def update(idx, delta):
    while idx < 100005:
        bit[idx] += delta
        idx += idx & (-idx)


def do_update(left, right, delta):
    update(left, +delta)
    update(right + 1, -delta)


def query(idx):
    tot = 0
    while idx > 0:
        tot += bit[idx]
        idx -= idx & (-idx)
    return tot


def main():
    global tempo
    n = int(input())
    for _ in range(n - 1):
        st, et = map(int, input().split())
        g[st].append(et)
        g[et].append(st)
    custo[:n] = map(int, input().split())
    dfs(1)
    for i in range(n):
        do_update(in_time[i + 1], in_time[i + 1], custo[i])

    q = int(input())
    for _ in range(q):
        line = list(map(int, input().split()))
        task = int(line[0])
        if task == 1:
            node, delta = line[1], line[2]
            start_node = in_time[node]
            end_node = out_time[node]
            do_update(start_node, end_node, +delta)
        elif task == 2:
            node, delta = line[1], line[2]
            do_update(in_time[node], in_time[node], +delta)
        elif task == 3:
            node = line[1]
            if blacklist[node] == -1:
                blacklist[node] = query(in_time[node])
            else:
                cur = query(in_time[node])
                replace = blacklist[node]
                do_update(in_time[node], in_time[node], -cur + replace)
                blacklist[node] = -1
        else:
            node = line[1]
            if blacklist[node] == -1:
                print(query(in_time[node]))
            else:
                print(blacklist[node])


if __name__ == "__main__":
    main()
