import time

lista_original = list(range(1, 1000001))
lista_auxiliar = set(range(1, 1000001, 2))

inicio = time.time()
########################
# Escribe tu codigo aqui

lista_nueva = [element for element in lista_original if element not in lista_auxiliar]

########################

fin = time.time()
print(fin - inicio)
