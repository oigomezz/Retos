import itertools

mod = 1000000007
n = int(input())
arr = list(map(int, input().split()))
subsets = list(
    map(lambda x: list(itertools.combinations(arr, x)), range(2, len(arr)+1)))

result = [item for sublist in subsets for item in sublist]

suma = 0
for element in result:
    suma += (max(element)) | min(element)

print(suma % mod)
