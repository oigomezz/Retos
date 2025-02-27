from collections import deque

a = [0] * 1010000
nge = [0] * 1010000
pge = [0] * 1010000

N = int(input())
arr = list(map(int, input().split()))
for i in range(1, N+1):
    a[i] = arr[i - 1]

st = deque()
st.append(1)
for i in range(2, N+1):
    while st and a[st[-1]] < a[i]:
        nge[st.pop()] = i
    st.append(i)

while st:
    nge[st.pop()] = -1

st = deque()
st.append(N)
for i in range(N-1, 0, -1):
    while st and a[st[-1]] < a[i]:
        pge[st.pop()] = i
    st.append(i)

while st:
    pge[st.pop()] = -1

for i in range(1, N+1):
    print(nge[i] + pge[i], end=" ")

print()
