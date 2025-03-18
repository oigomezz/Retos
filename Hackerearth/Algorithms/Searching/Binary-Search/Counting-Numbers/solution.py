class Node:
    __slots__ = "val", "left", "right"

    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None


def update(curr, index, left, right):
    if left == right:
        curr.val = 1
        return
    mid = (left + right) // 2
    if index <= mid:
        if not curr.left:
            curr.left = Node()
        update(curr.left, index, left, mid)
    else:
        if not curr.right:
            curr.right = Node()
        update(curr.right, index, mid + 1, right)
    curr.val = (curr.left.val if curr.left else 0) + \
        (curr.right.val if curr.right else 0)


def query(curr, val, left, right):
    if not curr:
        return val
    if left == right:
        return left
    mid = (left + right) // 2
    lval = curr.left.val if curr.left else 0
    now = mid - lval

    if val > now:
        return query(curr.right, val + lval, mid + 1, right)
    else:
        return query(curr.left, val, left, mid)


def max_k_len_nr(a, n, k):
    if k >= n:
        return a
    elif k <= 0:
        return ""
    stack = []
    for i, c in enumerate(a):
        while stack and c > stack[-1] and len(stack) > k - n + i:
            stack.pop()
        if len(stack) < k:
            stack.append(c)
    return "".join(stack)


def nxt_sm_nr(a, n):
    st = []
    for i in range(n - 1):
        if st and st[-1][0] < a[i]:
            while st and st[-1][0] < a[i]:
                yield st[-1][1]
                if st:
                    st.pop()
            st.append((a[i], i))
        elif a[i] < a[i + 1]:
            yield i
        else:
            st.append((a[i], i))
    last = True
    if a[i] >= a[i + 1]:
        last = False
        yield i + 1
    while st:
        if last and st[-1][0] >= a[i + 1]:
            last = False
            yield i + 1
        yield st[-1][1]
        st.pop()


def create_b(a, n):
    ixl = set()
    for ix in nxt_sm_nr(a, n):
        ixl.add(ix)
        b = ""
        for i in range(n):
            if i not in ixl:
                b += a[i]
        print(b)


def all_a(a):
    for i in nxt_sm_nr(a):
        print(i, end=" ")


def max_k_len_nr(a, n, k):
    if k >= n:
        return a
    elif k <= 0:
        return ""
    stack = []
    for i, c in enumerate(a):
        while stack and c > stack[-1] and len(stack) > k - n + i:
            stack.pop()
        if len(stack) < k:
            stack.append(c)
    return "".join(stack)


def all_max_k(a, n, k):
    for k in range(1, n + 1):
        print(" " * (n - k) + max_k_len_nr(a, n, k))


if __name__ == "__main__":
    a = input()
    n = len(a)
    m = int(input())
    ans = ""

    ql = []
    for m_ in range(m):
        k, l = [int(x) for x in input().split()]

        ql.append((k, l, m_))
    ql.sort(key=lambda x: x[0])
    res = dict()
    root = Node()
    next_number_gen = nxt_sm_nr(a, n)

    while ql and ql[-1][0] == n:
        res[ql[-1][2]] = a[ql[-1][1] - 1]

        ql.pop()
    curr_k = n

    while ql:
        next_k = ql[-1][0]
        while curr_k > next_k:
            ixr = next(next_number_gen)
            update(root, ixr + 1, 1, n)
            curr_k -= 1
        while ql and ql[-1][0] == curr_k:
            orig_ix = query(root, ql[-1][1], 1, n) - 1
            res[ql[-1][2]] = a[orig_ix]
            ql.pop()
    for m_ in range(m):
        ans += res[m_]
    print(ans)
