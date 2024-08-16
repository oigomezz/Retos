import itertools

n, k = map(int, input().split())
arr = list(map(int, input().split()))

subsets = list(
    map(lambda x: list(itertools.combinations(arr, x)), range(1, k+1)))
result = [item for sublist in subsets for item in sublist]


resultado = set()
for element in result:
    integer = 0
    for num in element:
        integer |= num
    resultado.add(integer)
print(len(resultado))
