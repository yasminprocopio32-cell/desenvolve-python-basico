frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
nova_frase = ""
for letra in frase:
    if letra in vogais:
        nova_frase += "*"
    else:
        nova_frase += letra
print(nova_frase)