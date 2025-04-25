n = int(input())
a = sorted(map(int, input().strip().split()))
left = 0
right = sum(a)
j = 0
temp = 0
ans = right
for i, element in enumerate(a):
    while a[j] < abs(element - a[j]):
        temp += a[j]
        j += 1
    count = temp
    count += (i - j) * element - left + temp
    count += right - (n - i) * element
    ans = min(ans, count)
    left += element
    right -= element

print(ans)
