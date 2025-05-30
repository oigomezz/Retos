from sortedcontainers import SortedSet

n = 0


class Graph:
    def __init__(self, new_n=0):
        self.n = new_n
        self.no_right_s = SortedSet()
        self.no_left_s = SortedSet()
        self.to_center_s = SortedSet()
        self.segments = []

    def change_edge(self, a, b):
        if a == self.n:
            self.to_center_s.discard(b)
        elif b == self.n:
            self.to_center_s.add(a)
        elif (a + 1) % self.n == b:
            self.no_right_s.discard(a)
            self.no_left_s.add(b)
        else:
            self.no_left_s.discard(a)
            self.no_right_s.add(b)

    def can_reach_center(self, a):
        if a == self.n:
            return True
        self.segments.clear()
        self.add_reachable_to_right(a)
        self.add_reachable_to_left(a)
        for segment in self.segments:
            l, r = segment
            it = self.to_center_s.irange(l, r)
            if any(True for _ in it):
                return True
        return False

    def add_reachable_to_right(self, a):
        if not self.no_right_s:
            self.segments.clear()
            self.segments.append((0, self.n - 1))
            return
        it = self.no_right_s.irange(a, None)
        next_no_right = next(it, None)
        if next_no_right is not None:
            self.segments.append((a, next_no_right))
            return
        self.segments.append((a, self.n - 1))
        if self.n - 1 in self.no_right_s or a == 0:
            return
        it = self.no_right_s.irange(0, None)
        first_no_right = next(it, None)
        if first_no_right is None:
            self.segments.append((0, a - 1))
        else:
            self.segments.append((0, first_no_right))

    def add_reachable_to_left(self, a):
        if not self.no_left_s:
            self.segments.clear()
            self.segments.append((0, self.n - 1))
            return
        it = self.no_left_s.irange(None, a)
        prev_no_left = None
        for no_left in it:
            prev_no_left = no_left
        if prev_no_left is not None:
            self.segments.append((prev_no_left, a))
            return
        self.segments.append((0, a))
        if 0 in self.no_left_s or a == self.n - 1:
            return
        last_no_left = self.no_left_s[-1]
        self.segments.append((last_no_left, self.n - 1))


graph = Graph()
reverse_graph = Graph()


def can_reach(a, b):
    can_reach_center_b = reverse_graph.can_reach_center(b)
    can_reach_center_a = graph.can_reach_center(a)
    if a == n:
        return can_reach_center_b
    if b == n:
        return can_reach_center_a
    if can_reach_center_a and can_reach_center_b:
        return True
    for segment in graph.segments:
        l, r = segment
        if l <= b <= r:
            return True
    return False


n = int(input())
graph = Graph(n)
reverse_graph = Graph(n)
for _ in range(2 * n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph.change_edge(a, b)
    reverse_graph.change_edge(b, a)

q = int(input())
for _ in range(q):
    type_query, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if type_query == 1:
        graph.change_edge(a, b)
        reverse_graph.change_edge(b, a)
    else:
        res = can_reach(a, b)
        print("Yes" if res else "No")
