def subconjuntos(numeros):
    return subconjuntos_recursivo([], sorted(numeros))


def subconjuntos_recursivo(actual, conjunto):
    if conjunto:
        return subconjuntos_recursivo(actual, conjunto[1:]) + subconjuntos_recursivo(actual + [conjunto[0]], conjunto[1:])
    return [actual]


if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().split()))
    subconjuntos = subconjuntos(arr)
    sub2 = []

    for sub in subconjuntos:
        if len(sub) > 1:
            sub2.append(sub)

    suma = 0
    for element in sub2:
        suma += max(element) | min(element)

    print(suma)
