Idade = int(input ("Digite sua idade: "))
jogou_3_ou_mais = input ("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")
venceu_vezes = int(input ("Quantas vezes já venceu? "))
jogou_3_ou_mais = jogou_3_ou_mais.strip().lower() == "true"
apto = (16 <= Idade <= 18 and (jogou_3_ou_mais or venceu_vezes > 0))
print ("Apto para ingressar no clube de jogos de tabuleiro: ", apto)
