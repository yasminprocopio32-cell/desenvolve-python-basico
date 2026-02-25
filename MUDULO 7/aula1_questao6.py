def encontrar_anagramas(texto, palavra_objetivo):
    tamanho = len(palavra_objetivo)
    alvo_ordenado = sorted(palavra_objetivo)
    anagramas = []

    for palavra in texto.split():
        if len(palavra) == tamanho and sorted(palavra) == alvo_ordenado:
            anagramas.append(palavra)

    return anagramas


texto = input("Digite o texto: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

print(encontrar_anagramas(texto, palavra_objetivo))