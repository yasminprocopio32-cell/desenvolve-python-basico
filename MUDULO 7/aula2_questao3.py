import re

while True:
    frase = input("Digite uma frase (ou 'Fim' para encerrar): ")
    
    if frase == "Fim":
        break
    
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()
    
    if frase_limpa == frase_limpa[::-1]:
        print("É palíndromo")
    else:
        print("Não é palíndromo")