import random

lista = [random.randint(-10, 10) for _ in range(20)]

print("Original:", lista)

inicio = fim = 0
max_inicio = max_fim = 0
max_tamanho = 0
i = 0

while i < len(lista):
    if lista[i] < 0:
        inicio = i
        while i < len(lista) and lista[i] < 0:
            i += 1
        fim = i
        if fim - inicio > max_tamanho:
            max_tamanho = fim - inicio
            max_inicio = inicio
            max_fim = fim
    else:
        i += 1

del lista[max_inicio:max_fim]

print("Editada: ", lista)
