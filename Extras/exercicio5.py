# Faça um programa que peça cinco números e mostre qual o maior e qual o menor

numero1 = input("Digite um número: ")
numero2 = input("Digite um número: ")

if numero1 > numero2:
    maiorNumero = numero1
    menorNumero = numero2

else:
    maiorNumero = numero2
    menorNumero = numero1
    
numero3 = input("Digite um número: ")
if numero3 > maiorNumero:
    maiorNumero = numero3
elif numero3 < menorNumero:
    menorNumero = numero3    

numero4 = input("Digite um número: ")
if numero4 > maiorNumero:
    maiorNumero = numero4
elif numero4 < menorNumero:
    menorNumero = numero4

numero5 = input("Digite um número: ")
if numero5 > maiorNumero:
    maiorNumero = numero5
elif numero5 < menorNumero:
    menorNumero = numero5

print('O maior numero é {maior} e o menor numero é o {menor}'.format(maior=maiorNumero, menor=menorNumero))