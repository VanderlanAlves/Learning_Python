#Faça um programa que peça uma frase para a pessoa e mostre a quantidade de letras que tem na frase.

frase = input("Digite a frase: ")

qtd_letras = len(frase)

print('A frase tem {qtd} letras'.format(qtd=qtd_letras))