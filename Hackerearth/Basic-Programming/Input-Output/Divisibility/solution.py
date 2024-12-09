N = int(input())
data = [x for x in input().split()]
number = int(data[N-1]) % 10

if number == 0:
    print("Yes")
else:
    print("No")
