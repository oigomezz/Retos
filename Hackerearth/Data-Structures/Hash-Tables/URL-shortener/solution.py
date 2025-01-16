def solve(n, query):
    histories = {}
    visited = set()
    for time, url, key, user_id in query:
        time = int(time)
        lk = len(key)
        if key in visited or lk < 2 or lk > 12:
            yield 'NO'
            continue
        if user_id in histories and time - histories[user_id] < 5:
            yield 'NO'
            continue
        if not (url.startswith('http://') or url.startswith('https://')):
            yield 'NO'
            continue
        if key.isalnum():
            visited.add(key)
        else:
            yield 'NO'
            continue
        histories[user_id] = time
        yield 'YES'


n = int(input())
query = [input().split() for _ in range(n)]

out_ = solve(n, query)
for i_out_ in out_:
    print(i_out_)
