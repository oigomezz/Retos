n = int(input())
powers = map(int, input().strip().split())
even = []
odd = []
for i in powers:
    if i % 2:
        odd.append(i)
    else:
        even.append(i)
even.sort()
odd.sort()
print(*even, sum(even), *odd, sum(odd))
