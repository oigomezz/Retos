import numpy

n, c = map(int, input().strip().split())
values = list(map(int, input().strip().split()))
weights = list(map(int, input().strip().split()))
dp = numpy.full(sum(values) + 1, 10 ** 18, dtype=numpy.int64)
dp[0] = 0
mx = 0
for v, w in zip(values, weights):
    numpy.minimum(dp[v:mx + v + 1], dp[:mx + 1] + w, out=dp[v:mx + v + 1])
    mx += v
print(numpy.nonzero(dp <= c)[0].max())
