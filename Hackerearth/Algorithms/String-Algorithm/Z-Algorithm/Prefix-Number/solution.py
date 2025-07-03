def calculate(N):
    ln = len(N)
    a = [0] * ln
    left = right = 0
    for i in range(1, ln):
        if i > right:
            left = right = i
            while right < ln and N[right - left] == N[right]:
                right += 1
            a[i] = right - left
            right -= 1
        else:
            if a[i - left] < right - i + 1:
                a[i] = a[i - left]
            else:
                left = i
                while right < ln and N[right - left] == N[right]:
                    right += 1
                a[i] = right - left
                right -= 1

    ways = 0
    for i in range(1, len(a)):
        ways += (a[i] >= i)

    return ways


N = input()

out_ = calculate(N)
print(out_)
