def find_k(k, score, n):
    # Write your code here
    pass


N, K = map(int, input().split())
score = list(map(int, input().split()))

out_ = find_k(K, score, N)
print(' '.join(map(str, out_)))
