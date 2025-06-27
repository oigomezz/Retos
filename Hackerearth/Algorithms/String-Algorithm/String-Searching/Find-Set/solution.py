N = int(input())
strings = [input() for _ in range(N)]

string_set = set(strings)
sorted_set = sorted(strings, key=len)
ans = 0

for idx in range(N):
    string = sorted_set[idx]
    if string in string_set:
        ans += 1
        for idx_ahead in range(idx+1, N):
            if sorted_set[idx_ahead] in string_set and string in sorted_set[idx_ahead]:
                string_set.remove(sorted_set[idx_ahead])

print(ans)
