def subconjuntos(numeros):
    return subconjuntos_recursivo([], sorted(numeros))


def subconjuntos_recursivo(actual, conjunto):
    if conjunto:
        return subconjuntos_recursivo(actual, conjunto[1:]) + subconjuntos_recursivo(actual + [conjunto[0]], conjunto[1:])
    return [actual]


if __name__ == "__main__":

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    subconjuntos = subconjuntos(arr)
    sub2 = []

    for sub in subconjuntos:
        if len(sub) <= k and len(sub) > 0:
            sub2.append(sub)

    resultado = set()
    for element in sub2:
        integer = 0
        for num in element:
            integer |= num
        resultado.add(integer)
    print(len(resultado))
