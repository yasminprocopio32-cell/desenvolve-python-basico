n = int(input("Digite a quantidade de pessoas: "))
soma = 0
contador = n
while contador > 0:
    idade = int(input("Digite a idade: "))
    soma = soma + idade 
    contador = contador - 1
media = soma / n
print ("A média das idades é:", media)
