from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = [int(input()) for _ in range(k)]

    st = deque()
    st1 = deque()
    pge = [-1] * n
    nge = [n] * n

    for i in range(n):
        while st and a[st[-1]] <= a[i]:
            st.pop()
        if st:
            pge[i] = st[-1]
        st.append(i)

    for j in range(n - 1, -1, -1):
        while st1 and a[st1[-1]] <= a[j]:
            st1.pop()
        if st1:
            nge[j] = st1[-1]
        st1.append(j)

    for i in range(k):
        x = q[i] - 1
        seg = nge[x] - pge[x] - 1
        print(str(seg))
