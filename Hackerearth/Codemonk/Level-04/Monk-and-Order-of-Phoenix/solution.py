from collections import deque

v = [[] for _ in range(100)]
st = deque()


def bs(i, val):
    l, r = 0, len(v[i])
    while l < r:
        mid = (l + r) // 2
        if v[i][mid] > val:
            r = mid
        else:
            l = mid + 1
    if l < len(v[i]) and v[i][l] > val:
        return l
    return -1


def check():
    cur = st[-1]
    for i in range(1, n):
        ans = bs(i, cur)
        if ans == -1:
            return False
        else:
            cur = v[i][ans]
    return True


n = int(input())
for i in range(n):
    line = list(map(int, input().split()))
    x = int(line[0])
    for j in range(x):
        y = int(line[j+1])
        v[i].append(y)
st.append(v[0][0])
for i in range(1, len(v[0])):
    if v[0][i] < st[-1]:
        st.append(v[0][i])
    else:
        st.append(st[-1])
q = int(input())
for i in range(q):
    line = list(map(int, input().split()))
    ind = int(line[0])
    if ind == 1:
        k, val = map(int, line[1:])
        k -= 1
        v[k].append(val)
        if k == 0:
            if val < st[-1]:
                st.append(val)
            else:
                st.append(st[-1])
    elif ind == 0:
        k = int(line[1])
        k -= 1
        v[k].pop()
        if k == 0:
            st.pop()
    else:
        if check():
            print("YES")
        else:
            print("NO")
