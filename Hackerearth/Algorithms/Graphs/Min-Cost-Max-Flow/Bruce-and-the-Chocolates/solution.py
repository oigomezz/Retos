from math import gcd

maxnodes = 405

nodes = maxnodes
prio = [0] * maxnodes
curflow = [0] * maxnodes
prevedge = [0] * maxnodes
prevnode = [0] * maxnodes
q = [0] * maxnodes
pot = [0] * maxnodes
inqueue = [False] * maxnodes

class Edge:
    def __init__(self, to, f, cap, cost, rev):
        self.to = to
        self.f = f
        self.cap = cap
        self.cost = cost
        self.rev = rev

graph = [[] for _ in range(maxnodes)]

def add_edge(source, target, capacity, cost):
    edge_a = Edge(target, 0, capacity, cost, len(graph[target]))
    edge_b = Edge(source, 0, 0, -cost, len(graph[source]))
    graph[source].append(edge_a)
    graph[target].append(edge_b)

def bellman_ford(source, dist):
    for i in range(nodes):
        dist[i] = float('inf')
    dist[source] = 0
    qt = 0
    q[qt] = source
    qt += 1
    for qh in range(nodes * 2):
        u = q[qh % nodes]
        inqueue[u] = False
        for i in range(len(graph[u])):
            edge = graph[u][i]
            if edge.cap <= edge.f:
                continue
            v = edge.to
            ndist = dist[u] + edge.cost
            if dist[v] > ndist:
                dist[v] = ndist
                if not inqueue[v]:
                    inqueue[v] = True
                    q[qt % nodes] = v
                    qt += 1

def min_cost_flow(source, target, max_flow):
    bellman_ford(source, pot)
    flow = 0
    flow_cost = 0
    while flow < max_flow:
        q = []
        q.append((0, source))
        for i in range(nodes):
            prio[i] = float('inf')
        prio[source] = 0
        curflow[source] = float('inf')
        while q:
            current = q.pop(0)
            d = current[0]
            u = current[1]
            if d != prio[u]:
                continue
            for i in range(len(graph[u])):
                edge = graph[u][i]
                v = edge.to
                if edge.cap <= edge.f:
                    continue
                nprio = prio[u] + edge.cost + pot[u] - pot[v]
                if prio[v] > nprio:
                    prio[v] = nprio
                    q.append((nprio, v))
                    prevnode[v] = u
                    prevedge[v] = i
                    curflow[v] = min(curflow[u], edge.cap - edge.f)
        if prio[target] == float('inf'):
            break
        for i in range(nodes):
            pot[i] += prio[i]
        df = min(curflow[target], max_flow - flow)
        flow += df
        v = target
        while v != source:
            edge = graph[prevnode[v]][prevedge[v]]
            edge.f += df
            graph[v][edge.rev].f -= df
            flow_cost += df * edge.cost
            v = prevnode[v]
    return (flow, flow_cost)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        for i in range(maxnodes):
            graph[i].clear()
        inqueue = [False] * maxnodes

        n, m = map(int, input().split())
        n -= 1
        a = [0] * 206
        arr = list(map(int, input().split()))
        for i in range(1, n + 1):
            a[i] = arr[i-1]
        
        cost = [[0] * 205 for _ in range(205)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                cost[i][j] = 0
        
        for _ in range(m):
            a1, b = map(int, input().split())
            if a1 % 2 == 0:
                a1, b = b, a1
            cost[a1][b] = gcd(a[a1], a[b])

        for i in range(1, n + 1, 2):
            for j in range(2, n + 1, 2):
                add_edge(i, j, 1, 1e5 - cost[i][j])

        for i in range(1, n + 1, 2):
            add_edge(0, i, 1, 0)
            add_edge(i + 1, 404, 1, 0)

        result = min_cost_flow(0, 404, float('inf'))
        print(int(1e5 * result[0] - result[1]))