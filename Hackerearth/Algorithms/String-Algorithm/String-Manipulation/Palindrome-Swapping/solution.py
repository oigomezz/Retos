def make_equal(first, second):
    n = len(first)
    m = n // 2
    if n % 2 and second[m] != first[m]:
        return "NO"
    for i in range(m):
        j = n - i - 1
        if not ((second[i] == second[j] and first[i] == first[j]) or
                (second[i] == first[i] and second[j] == first[j]) or
                (second[i] == first[j] and second[j] == first[i])):
            return "NO"
    return "YES"


first = input()
second = input()

out_ = make_equal(first, second)
print(out_)
