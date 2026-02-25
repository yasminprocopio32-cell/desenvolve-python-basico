import random

def encrypt(lista):
    n = random.randint(1, 10)
    resultado = []
    
    for nome in lista:
        novo = ""
        for c in nome:
            codigo = ord(c)
            if 33 <= codigo <= 126:
                novo_codigo = 33 + ((codigo - 33 + n) % 94)
                novo += chr(novo_codigo)
            else:
                novo += c
        resultado.append(novo)
    
    return resultado, n

nomes = ["Ana", "Carlos", "Beatriz"]
criptografados, chave = encrypt(nomes)

print("Criptografados:", criptografados)
print("Chave:", chave)


