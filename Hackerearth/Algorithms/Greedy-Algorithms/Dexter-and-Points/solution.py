n = int(input())
array = map(int, input().split())
num = 1
for i in array:
    num = num * ((pow(i + 1, 2) + 1) // 2) % 1000000007
print(num)
