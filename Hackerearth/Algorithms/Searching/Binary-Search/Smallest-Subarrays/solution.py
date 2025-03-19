def update(list, n, index):
    while index <= n:
        list[index] += 1
        index += index & -index


def query(list, index):
    ans = 0
    while index:
        ans += list[index]
        index -= index & -index
    return ans


def solution(n, arr_a, arr_b):
    n1 = n+1
    n2 = n+2
    a = [(0, 0)]
    for i in range(1, n1):
        a.append((arr_a[i], i))
    a = [a[0]]+sorted(a[1:], reverse=True)
    lista = [0]*(n1)
    ans = ["-1"]*(n1)
    for i in range(1, n1):
        ai_position = a[i][1]
        temp = n1-ai_position
        update(lista, n, temp)
        if arr_b[ai_position] > n1-ai_position:
            continue
        count = query(lista, temp)
        if arr_b[ai_position] <= count:
            low = 1
            high = temp
            minimo = count-arr_b[ai_position]
            while low < high:
                mid = (high+low)//2
                if query(lista, mid) <= minimo:
                    low = mid+1
                else:
                    high = mid
            ans[ai_position] = str(n2-low-ai_position)
    print(" ".join(ans[1:]))


if __name__ == '__main__':
    n = int(input())
    A = [0]+[int(x) for x in input().split()]
    B = [0]+[int(x) for x in input().split()]
    solution(n, A, B)
