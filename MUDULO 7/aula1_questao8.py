cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ").strip()

cpf_numeros = cpf.replace(".", "").replace("-", "")

if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
    print("Inválido")
else:
    if cpf_numeros == cpf_numeros[0] * 11:
        print("Inválido")
    else:
        # Primeiro dígito
        soma1 = sum(int(cpf_numeros[i]) * (10 - i) for i in range(9))
        resto1 = soma1 % 11
        dig1 = 0 if resto1 < 2 else 11 - resto1

        # Segundo dígito
        soma2 = sum(int(cpf_numeros[i]) * (11 - i) for i in range(10))
        resto2 = soma2 % 11
        dig2 = 0 if resto2 < 2 else 11 - resto2

        if cpf_numeros[-2:] == f"{dig1}{dig2}":
            print("Válido")
        else:
            print("Inválido")