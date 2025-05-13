n = int(input())
degrees = map(int, input().split())
if sum(degrees) == 2 * (n - 1):
    print('Yes')
else:
    print('No')
