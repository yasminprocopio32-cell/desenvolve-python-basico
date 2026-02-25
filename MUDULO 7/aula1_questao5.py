frase = input("Digite a frase: ")

vogais = "aeiouAEIOU"
indices = []

for i, letra in enumerate(frase):
    if letra in vogais:
        indices.append(i)

print("Quantidade de vogais:", len(indices))
print("Índices das vogais:", indices)