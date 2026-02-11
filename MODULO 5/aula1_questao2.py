import random
import math
n = int(input("Digite a quantidade de valores: "))
soma = 0
for i in range(n):
    valor = random.randint(0, 100)
    soma += valor
    print(f"Valor gerado {i + 1}: {valor}")
resultado = math.sqrt(soma)
print(f"\nSoma dos valores: {soma}")
print(f"Raiz quadrada da soma: {resultado}")
