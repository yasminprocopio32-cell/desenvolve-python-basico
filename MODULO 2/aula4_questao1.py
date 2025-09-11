#Ler o comprimento do terreno (em metros)
comprimento = int(input("Digite o comprimento do terreno (em metros): "))
#Ler a largura do terreno (em metros)
largura = int (input ("Digite a largura do terreno (em metros):"))
#Ler o preço do metro quadrado (em reais)
preco_m2 = float(input("Digite o preço do metro quadrado (em R$): "))
#Calcular a área do terreno
area_m2 = comprimento * largura
#Calcular o valor total do terreno
preco_total = preco_m2 * area_m2
#Exibir o resultado no formato solicitado
print (f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")

