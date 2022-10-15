# Faça um programa que peça o nome da pessoa e a idade e diga se a pessoa já pode votar, se a pessoa já pode obter a carta de motorista.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print('Você pode votar e dirigir.')

elif idade >= 16 and idade < 18:
    print('Você só pode votar.')

else: 
    print('Você não pode votar nem dirigir.')


