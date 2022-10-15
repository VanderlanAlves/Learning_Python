# Crie uma função que recebe um número de CPF sem pontos e traço e RETORNE o número formatado

CPF = input("Digite um CPF:")

def formata_cpf(CPF):

    print(f"Seu CPF formatado é: {CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:11]}")

formata_cpf(CPF)