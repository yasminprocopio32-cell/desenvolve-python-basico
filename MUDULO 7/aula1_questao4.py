numero = input("Digite o número de celular: ").strip()

numero = numero.replace("-", "").replace(" ", "")

if len(numero) == 8:
    numero = "9" + numero
elif len(numero) == 9 and numero[0] != "9":
    print("Número inválido")
    exit()

numero_formatado = numero[:5] + "-" + numero[5:]

print(numero_formatado)