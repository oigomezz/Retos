from collections import defaultdict

N = 300005
M = 10**9 + 7

g = defaultdict(list)
vp = [(0, 0)] * N


def dfs(node, par):
    child = 0
    mx = 0
    nmx = 0
    for it in g[node]:
        if it != par:
            child += 1
            dfs(it, node)
            if vp[it][0] > mx:
                mx = vp[it][0]
                nmx = vp[it][1]
            elif vp[it][0] == mx:
                nmx += vp[it][1]
    if child == 0:
        vp[node] = (1, 1)
    else:
        vp[node] = (mx + 1, nmx)


def dfs_ans(node, par, up, cnt):
    vpr = []
    for it in g[node]:
        if it != par:
            vpr.append(vp[it])

    vpr.append((up, cnt))
    vpr.sort(reverse=True)

    case = 0
    suma = 0
    prod = 0
    sz = len(vpr)
    if sz == 0:
        cur = (1, 1)
    elif sz == 1:
        cur = vpr[0]
        cur = (cur[0] + 1, cur[1])
        case = 4
    else:
        if vpr[0][0] == vpr[1][0]:
            case = 1
            pos = 1
            while pos + 1 < sz and vpr[pos + 1][0] == vpr[pos][0]:
                pos += 1

            suma = 0
            prod = 0
            for i in range(pos + 1):
                prod += suma * vpr[i][1]
                suma += vpr[i][1]
            cur = (vpr[0][0] * 2 + 1, prod)
        elif sz > 2 and vpr[1][0] == vpr[2][0]:
            case = 2
            pos = 2
            while pos + 1 < sz and vpr[pos + 1][0] == vpr[pos][0]:
                pos += 1
            suma = 0
            for i in range(1, pos + 1):
                suma += vpr[i][1]
            cur = (vpr[0][0] + vpr[1][0] + 1, suma * vpr[0][1])
        else:
            case = 3
            cur = (vpr[0][0] + vpr[1][0] + 1, vpr[0][1] * vpr[1][1])

    vp[node] = cur

    for it in g[node]:
        if it != par:
            if case == 4:
                dfs_ans(it, node, 1, 1)
            elif case == 3:
                if vp[it] == vpr[0]:
                    dfs_ans(it, node, vpr[1][0] + 1, vpr[1][1])
                else:
                    dfs_ans(it, node, vpr[0][0] + 1, vpr[0][1])
            elif case == 2:
                if vp[it] == vpr[0]:
                    dfs_ans(it, node, vpr[1][0] + 1, suma)
                else:
                    dfs_ans(it, node, vpr[0][0] + 1, vpr[0][1])
            elif case == 1:
                if vp[it][0] == vpr[0][0]:
                    dfs_ans(it, node, vpr[0][0] + 1, suma - vp[it][1])
                else:
                    dfs_ans(it, node, vpr[0][0] + 1, suma)


if __name__ == "__main__":
    n = int(input())
    for _ in range(n - 1):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    dfs(1, -1)
    dfs_ans(1, -1, 0, 1)

    for i in range(1, n + 1):
        print(vp[i][0], vp[i][1])
