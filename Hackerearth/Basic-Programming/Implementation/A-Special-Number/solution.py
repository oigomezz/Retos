def suma_de_digitos(numero):
    numero = str(numero)
    suma = 0
    for i in numero:
        suma += int(i)
    return suma


t = int(input())
for _ in range(t):
    a = input().strip()
    suma = suma_de_digitos(a)
    while suma % 4 != 0:
        a = int(a)
        a += 1
        suma = suma_de_digitos(a)
    print(a)
