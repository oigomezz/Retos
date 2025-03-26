from collections import defaultdict

testcases = int(input())
occurrences = defaultdict(list)
for i in range(testcases):
    string_input = input()
    occurrences[string_input].append(i + 1)

queries = int(input())
for _ in range(queries):
    a, b, query = map(str, input().split())
    a = int(a)
    b = int(b)
    start = next((i for i, value in enumerate(occurrences[query]) if value >= a), len(occurrences[query]))
    end = next((i for i, value in enumerate(occurrences[query]) if value > b), len(occurrences[query]))

    print(end - start)
