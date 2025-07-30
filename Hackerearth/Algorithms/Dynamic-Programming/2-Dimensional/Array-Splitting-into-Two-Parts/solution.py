def find_answer(arr):
    return int((sum(arr) / 2) ** 2)


N = int(input())
A = map(int, input().split())

out_ = find_answer(A)
print(out_)
