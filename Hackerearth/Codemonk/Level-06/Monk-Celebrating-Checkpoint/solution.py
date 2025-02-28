n, m, k = list(map(int, input().strip().split(" ")))
arr = list(map(int, input().strip().split(" ")))

minArr = [-1]*n
maxArr = [-1]*n
stack = []

for i in range(0, len(arr)):
    while len(stack) > 0 and arr[stack[-1]] < arr[i]:
        maxArr[stack.pop()] = i
    stack.append(i)

while stack:
    maxArr[stack.pop()] = n

stack = []
for i in range(0, len(arr)):
    while len(stack) > 0 and arr[stack[-1]] > arr[i]:
        minArr[stack.pop()] = i
    stack.append(i)

while stack:
    minArr[stack.pop()] = n

minArr_left = [-1]*n
maxArr_left = [-1]*n

stack = [n-1]
for i in range(n-2, -1, -1):
    while stack and arr[stack[-1]] > arr[i]:
        minArr_left[stack.pop()] = i
    stack.append(i)

while stack:
    minArr_left[stack.pop()] = -1

stack = [n-1]
for i in range(n-2, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
        maxArr_left[stack.pop()] = i
    stack.append(i)


while stack:
    maxArr_left[stack.pop()] = -1


MIN_arr = []
MAX_arr = []
diffArr = []
countArr = []

maxval = -99
maxind = 0
ans = 0

for i in range(len(arr)):
    k = (minArr[i]-i)*(i-minArr_left[i])
    MIN_arr.append(k)
    l = (maxArr[i]-i)*(i-maxArr_left[i])
    MAX_arr.append(k)
    diffArr.append(l-k)
    ans += diffArr[i]*arr[i]

diffArr.sort(reverse=True)
for index in range(0, m):
    if diffArr[index] > 0:
        ans += diffArr[index]

print(ans)
