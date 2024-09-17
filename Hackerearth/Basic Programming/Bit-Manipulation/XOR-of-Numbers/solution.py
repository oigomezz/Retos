n, q = map(int, input().split())
array = list(map(int, input().split()))

prefix_xor = [0] * (n + 1)
for i in range(n):
    prefix_xor[i + 1] = prefix_xor[i] ^ array[i]

results = []
for _ in range(q):
    left, right = map(int, input().split())
    results.append(prefix_xor[-1] ^ prefix_xor[right] ^ prefix_xor[left-1])

print("\n".join(map(str, results)))
