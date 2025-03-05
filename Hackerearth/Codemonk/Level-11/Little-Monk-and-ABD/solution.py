n = int(input())
scores = list(map(lambda x: int(x), input().split()))
sorted_scores = sorted(scores)
queries = int(input())
for i in range(queries):
    k = input().split()
    if (k[1] == 'L'):
        print(sorted_scores[n-int(k[0])])
    else:
        print(sorted_scores[int(k[0])-1])
