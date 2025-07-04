from collections import defaultdict
from bisect import bisect_left


class SegmentTree1:
    def __init__(self, data, default=float("inf"), func=min):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for idx in reversed(range(_size)):
            self.data[idx] = func(self.data[idx + idx],
                                  self.data[idx + idx + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(
                self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        if start == stop:
            return self.__getitem__(start)
        stop += 1
        start += self._size
        stop += self._size

        response = self._default
        while start < stop:
            if start & 1:
                response = self._func(response, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                response = self._func(response, self.data[stop])
            start >>= 1
            stop >>= 1
        return response

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


n, q = map(int, input().split())
arr = list(map(int, input().split()))
res = [0]*(n+2)
d = defaultdict(list)
where = [n]*(n+1)
stack = []
for i in range(n-1, -1, -1):
    if not stack:
        stack.append(i)
    else:
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if not stack:
            stack.append(i)
        else:
            where[i] = stack[-1]
            stack.append(i)


for i, el in enumerate(arr):
    d[el].append(i)
for i in range(n-1, -1, -1):
    el = arr[i]
    ind = where[i]
    res[i] = (ind-i)*(arr[i])+res[ind]
e = SegmentTree1(arr)
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    t = e.query(l, r)
    p = bisect_left(d[t], r)
    if p == len(d[t]) or d[t][p] != t:
        p -= 1
    ind = where[d[t][p]]
    print(res[l]-t*(ind-r-1)-res[ind])
