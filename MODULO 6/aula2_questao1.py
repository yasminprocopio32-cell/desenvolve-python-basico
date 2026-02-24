import random

lista = [random.randint(-100, 100) for _ in range(20)]
lista_ordenada = sorted(lista)

maior_valor = max(lista)
menor_valor = min(lista)

indice_maior = lista.index(maior_valor)
indice_menor = lista.index(menor_valor)

print(lista_ordenada)
print(lista)
print(indice_maior)
print(indice_menor)