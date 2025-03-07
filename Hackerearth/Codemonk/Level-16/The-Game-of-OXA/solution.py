pow2 = {i: 1 << i for i in range(17)}


def get_max_oxa(n, arr):
    max_oxa = 0
    for k in range(1, 2**n):
        subarray = [arr[i] for i in range(n) if (k & pow2[i]) > 0]
        oxa = subarray[0]
        j = 0
        if len(subarray) > 1:
            for a in subarray[1:]:
                if j == 0:
                    oxa = oxa | a
                elif j == 1:
                    oxa = oxa ^ a
                else:
                    oxa += a
                j = (j + 1) % 3
        max_oxa = max(max_oxa, oxa)
    return max_oxa


for t in range(int(input())):
    prediction = input().strip()
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    max_oxa = get_max_oxa(n, arr)
    parity = "Even" if max_oxa % 2 == 0 else "Odd"
    print("Monk" if prediction == parity else "Mariam")
