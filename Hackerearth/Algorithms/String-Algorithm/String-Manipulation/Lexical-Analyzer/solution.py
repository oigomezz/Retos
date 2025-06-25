n = int(input())
variables = set()
for _ in range(n):
    variables.add(input().strip().split('=')[0])
print(len(variables))
