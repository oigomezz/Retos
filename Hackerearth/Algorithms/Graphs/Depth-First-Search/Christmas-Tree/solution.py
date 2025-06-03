import threading
import bisect
import sys


class InputReader:
    def __init__(self, stream):
        self.stream = stream
        self.buffer = []
        self.index = 0

    def next(self):
        while self.index >= len(self.buffer):
            line = self.stream.readline()
            if not line:
                raise EOFError()
            self.buffer = line.strip().split()
            self.index = 0

        token = self.buffer[self.index]
        self.index += 1
        return token

    def next_int(self):
        return int(self.next())


class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight


class ChristmasTree:
    def __init__(self):
        self.n = 0
        self.graph = None
        self.nidx = 0
        self.MAXN = 750001
        self.LOG = 21
        self.MAXM = 18000000

        # Initialize arrays
        self.nleft = [0] * self.MAXM
        self.nright = [0] * self.MAXM
        self.nsum = [0] * self.MAXM
        self.anc = [[0] * self.MAXN for _ in range(self.LOG)]
        self.gdepth = [0] * self.MAXN
        self.cnodes = [0] * self.MAXN
        self.queue = [0] * self.MAXN
        self.root = 0

    def init(self):
        # Arrays.fill(gdepth, 1 << 29);
        for i in range(len(self.gdepth)):
            self.gdepth[i] = 1 << 29

        front = 0
        back = 0
        self.gdepth[0] = 0
        self.queue[back] = 0
        back += 1
        self.anc[0][0] = -1
        self.cnodes[0] = self.build(0, self.n - 1)

        while front != back:
            node = self.queue[front]
            front += 1
            for e in self.graph[node]:
                if self.gdepth[node] + 1 < self.gdepth[e.to]:
                    self.gdepth[e.to] = self.gdepth[node] + 1
                    self.anc[0][e.to] = node
                    self.queue[back] = e.to
                    back += 1
                    self.cnodes[e.to] = self.inc(e.weight, self.cnodes[node])

        k = 1
        while (1 << k) < self.n:
            for i in range(self.n):
                if self.anc[k - 1][i] == -1:
                    self.anc[k][i] = -1
                else:
                    self.anc[k][i] = self.anc[k - 1][self.anc[k - 1][i]]
            k += 1

    def lca(self, a, b):
        if self.gdepth[a] < self.gdepth[b]:
            t = a
            a = b
            b = t

        diff = self.gdepth[a] - self.gdepth[b]
        i = 0
        while (1 << i) <= diff:
            if ((diff) & (1 << i)) != 0:
                a = self.anc[i][a]
            i += 1

        if a == b:
            return a

        for i in range(self.LOG - 1, -1, -1):
            if self.anc[i][a] != self.anc[i][b]:
                a = self.anc[i][a]
                b = self.anc[i][b]

        return self.anc[0][a]

    def solve(self, input_reader, output_writer):
        self.n = input_reader.nextInt()
        self.graph = [[] for _ in range(self.n)]

        weightmap = [0] * (self.n - 1)
        for i in range(self.n - 1):
            a = input_reader.nextInt() - 1
            b = input_reader.nextInt() - 1
            c = input_reader.nextInt()
            weightmap[i] = c
            self.graph[a].append(Edge(b, c))
            self.graph[b].append(Edge(a, c))

        weightmap.sort()

        for i in range(self.n):
            for e in self.graph[i]:
                e.weight = bisect.bisect_left(weightmap, e.weight)

        self.nidx = 0
        self.init()
        lastans = 0
        q = input_reader.nextInt()
        sb = []

        while q > 0:
            q -= 1
            a = input_reader.nextInt() - 1
            b = input_reader.nextInt() - 1
            k = input_reader.nextInt() - 1
            a = (a + lastans) % self.n
            b = (b + 2 * lastans) % self.n
            k = (k + 3 * lastans) % self.n

            r = self.lca(a, b)
            g = self.find_kth(
                self.cnodes[a], self.cnodes[b], self.cnodes[r], k)
            if g == -1:
                sb.append("-1\n")
                lastans = 0
            else:
                sb.append(str(weightmap[g]))
                sb.append("\n")
                lastans = weightmap[g] % self.n

        output_writer.write(''.join(sb))

    def build(self, left, right):
        if left == right:
            return self.create_node(0)
        mid = (left + right) >> 1
        return self.create_node(self.build(left, mid), self.build(mid + 1, right))

    def find_kth(self, apath, bpath, lcapath, k):
        if self.nsum[apath] + self.nsum[bpath] - 2 * self.nsum[lcapath] <= k:
            return -1
        left = 0
        right = self.n - 1
        while left != right:
            mid = (left + right) // 2
            d = self.nsum[self.nleft[apath]] + self.nsum[self.nleft[bpath]
                                                         ] - 2 * self.nsum[self.nleft[lcapath]]
            if d > k:
                apath = self.nleft[apath]
                bpath = self.nleft[bpath]
                lcapath = self.nleft[lcapath]
                right = mid
            else:
                k -= d
                apath = self.nright[apath]
                bpath = self.nright[bpath]
                lcapath = self.nright[lcapath]
                left = mid + 1
        return left

    def inc(self, pos, root):
        return self.inc_helper(pos, root, 0, self.n - 1)

    def inc_helper(self, pos, root, left, right):
        if left == right:
            return self.create_node(self.nsum[root] + 1)
        mid = (left + right) >> 1
        if pos <= mid:
            return self.create_node(self.inc_helper(pos, self.nleft[root], left, mid), self.nright[root])
        else:
            return self.create_node(self.nleft[root], self.inc_helper(pos, self.nright[root], mid + 1, right))

    def create_node(self, value_or_left, right=None):
        if right is None:
            # create_node(int value)
            value = value_or_left
            self.nleft[self.nidx] = -1
            self.nright[self.nidx] = -1
            self.nsum[self.nidx] = value
            self.nidx += 1
            return self.nidx - 1
        else:
            # create_node(int left, int right)
            left = value_or_left
            self.nleft[self.nidx] = left
            self.nright[self.nidx] = right
            self.nsum[self.nidx] = self.nsum[left] + self.nsum[right]
            self.nidx += 1
            return self.nidx - 1


if __name__ == "__main__":
    input_stream = sys.stdin
    output_stream = sys.stdout
    input_reader = InputReader(input_stream)

    def solve():
        tree = ChristmasTree()
        tree.solve(input_reader, output_stream)
        output_stream.flush()

    max_memory = 1024 * 1024 * 1024
    t = threading.Thread(target=solve)
    sys.setrecursionlimit(max_memory // 1000)
    t.start()
    t.join()
