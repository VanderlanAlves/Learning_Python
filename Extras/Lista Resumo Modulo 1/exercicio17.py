# Crie um programa que define uma função que recebe o ano de nascimento de uma pessoa e 
# mostre a idade atual de acordo com o ano atual.

def calcularIdade(idade):
    anoAtual = 2022
    valor_idade = anoAtual - idade
    
    return valor_idade

idade = int(input("Digite o ano do seu nascimento: "))

print(f"Você tem {calcularIdade(idade)} anos.")