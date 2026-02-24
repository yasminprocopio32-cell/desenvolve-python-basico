import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(list(set(lista1) & set(lista2)))

print("lista1:", lista1)
print("lista2:", lista2)
print("interseccao:", interseccao)
print("Contagem")

for elemento in interseccao:
    print(f"{elemento}: (lista1={lista1.count(elemento)}, lista2={lista2.count(elemento)})")