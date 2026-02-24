numeros = []

while True:
    entrada = input()
    if entrada.lower() == "fim":
        if len(numeros) >= 4:
            break
        else:
            continue
    try:
        numeros.append(int(entrada))
    except ValueError:
        pass

print(numeros)
print(numeros[:3])
print(numeros[-2:])
print(numeros[::-1])
print(numeros[::2])
print(numeros[1::2])