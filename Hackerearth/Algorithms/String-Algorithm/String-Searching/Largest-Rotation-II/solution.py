def min_cyclic_string(string):
    string += string
    n = len(string)
    i = 0
    ans = 0
    while i < n // 2:
        ans = i
        j = i + 1
        k = i
        while j < n and string[k] >= string[j]:
            if string[k] > string[j]:
                k = i
            else:
                k += 1
            j += 1
        while i <= k:
            i += j - k
    return string[ans:ans + n // 2]


if __name__ == "__main__":
    s = input().strip()
    print(min_cyclic_string(s))
