import collections
import sys

sys.setrecursionlimit(10**6)


class Graph:
    def __init__(self, n):
        self.adj_list = collections.defaultdict(list)
        self.edges = {}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        self.edges[(u, v)] = True
        self.edges[(v, u)] = True

    def find_diameter_in_dsu(self, li, mid):
        self.done = {}
        self.active_nodes = {}.fromkeys([node for _, node in li[:mid+1]], True)
        max_day = 0
        for _, node in li[:mid+1]:
            if node in self.done:
                continue
            self.diameter = 0
            self.get_max_depth(node, -1)
            max_day = max(max_day, self.diameter)
        return max_day

    def get_max_depth(self, node, par_node):
        mx, smx = 0, 0
        self.done[node] = True
        for cnode in self.adj_list[node]:
            if cnode == par_node:
                continue
            if self.is_connected(cnode, node):
                curr_depth = self.get_max_depth(cnode, node)
                if curr_depth >= mx:
                    mx, smx = curr_depth, mx
                elif curr_depth > smx:
                    smx = curr_depth

        self.diameter = max(self.diameter, mx + smx)
        return max(mx, smx) + 1

    def is_connected(self, u, v):
        if u not in self.active_nodes:
            return False
        if v not in self.active_nodes:
            return False
        if (u, v) not in self.edges:
            return False
        return True


N, K = map(int, input().split())
W = list(map(int, input().split()))
allEdges = []
tree = Graph(N)
for i in range(1, N):
    u, v = map(int, input().split())
    allEdges.append((u, v))
    tree.add_edge(u, v)


def solve(li):
    low, high = 0, N
    ans = -1
    while low < high:
        mid = (low + high)//2
        weight = li[mid][0]
        curr_diameter = tree.find_diameter_in_dsu(li, mid)
        if curr_diameter >= K:
            ans = weight
            high = mid
        else:
            low = mid+1
    return ans


li = [(weight, node+1) for node, weight in enumerate(W)]
li.sort()
print(solve(li))
