classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").strip().lower()
forca = int(input ("Digite os pontos de forca (1 a 20):"))
magia = int (input("Digite os pontos de magia (1 a 20): "))
if classe == "guerreiro" : valido = (forca >= 15) and (magia <=10)
elif classe == "mago" : valido = (forca <= 10) and (magia >= 15)
elif classe == "arqueiro" : valido = (forca >= 5) and (magia >= 5) and (forca <= 15) and (magia <= 15)
else: valido = False 
print ("Pontos de atributo consistentes com a classe escolhida:", valido)
