def solve(string, k):
    final_string = list(string)
    for i in range(len(final_string)):
        substring = final_string[i:i+k]
        for j in range(1, len(substring)):
            if substring[j] == substring[0]:
                substring[j] = "#"
        final_string[i:i+k] = substring
    return final_string.count("#")


S = input()
K = int(input())

out_ = solve(S, K)
print(out_)
