for _ in range(1):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 10**18

    suma = sum(A)
    left_sum = 0
    rno = n
    lno = 0

    j = 0
    count = 0

    for i in range(A[0], A[-1]+1):
        while (j < n and A[j] <= i+k):
            suma -= A[j]
            rno -= 1
            j += 1

        while (A[count] < i):
            left_sum += A[count]
            lno += 1
            count += 1

        ans = min(ans,  max(i*lno - left_sum, suma - rno*(i+k)))

    print(ans)
