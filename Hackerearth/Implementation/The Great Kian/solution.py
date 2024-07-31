n = int(input())
a = [int(x) for x in input().split()]
print(sum(a[0::3]), sum(a[1::3]), sum(a[2::3]))
