n1 = float(input("Digite n1: "))
n2 = float(input("Digite n2: "))
n3 = float(input("Digite n3: "))

m = (n1 + n2 + n3) / 3

if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

print("Fim")