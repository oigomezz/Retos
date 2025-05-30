def summon_the_spells(string_s, num_a, num_h):
    yield ''.join(str((int(c) + num_a) % 10) if i % 2 else c for i, c in enumerate(string_s))
    rotate_by = num_h % len(string_s)
    if rotate_by:
        yield string_s[(-rotate_by):] + string_s[:len(string_s) - rotate_by]


t = int(input())
for _ in range(t):
    s = input().strip()
    a, h = map(int, input().strip().split())
    visited = set()
    stack = [s]
    while stack:
        string = stack.pop()
        visited.add(string)
        for new_string in summon_the_spells(string, a, h):
            if new_string not in visited:
                stack.append(new_string)
                visited.add(new_string)
    print(min(visited))
