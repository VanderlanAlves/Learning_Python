# Receba dez números do usuário, e no final mostre qual o maior, qual o menor, e qual a média dos números.

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))
numero3 = float(input("Digite um número: "))
numero4 = float(input("Digite um número: "))
numero5 = float(input("Digite um número: "))
numero6 = float(input("Digite um número: "))
numero7 = float(input("Digite um número: "))
numero8 = float(input("Digite um número: "))
numero9 = float(input("Digite um número: "))
numero10 = float(input("Digite um número: "))

if numero1 > numero2:
    maiorNumero = numero1
    menorNumero = numero2
else:
    maiorNumero = numero2
    menorNumero = numero1

if numero3 > maiorNumero:
    maiorNumero = numero3
elif numero3 < menorNumero:
    menorNumero = numero3

if numero4 > maiorNumero:
    maiorNumero = numero4
elif numero4 < menorNumero:
    menorNumero = numero4

if numero5 > maiorNumero:
    maiorNumero = numero5
elif numero5 < menorNumero:
    menorNumero = numero5

if numero6 > maiorNumero:
    maiorNumero = numero6
elif numero6 < menorNumero:
    menorNumero = numero6

if numero7 > maiorNumero:
    maiorNumero = numero7
elif numero7 < menorNumero:
    menorNumero = numero7

if numero8 > maiorNumero:
    maiorNumero = numero8
elif numero8 < menorNumero:
    menorNumero = numero8

if numero9 > maiorNumero:
    maiorNumero = numero9
elif numero9 < menorNumero:
    menorNumero = numero9

if numero10 > maiorNumero:
    maiorNumero = numero10
elif numero10 < menorNumero:
    menorNumero = numero10

media = (numero1 + numero2 + numero3 + numero4 + numero5 + numero6 + numero7 + numero8 + numero9 + numero10) / 10

print(f"A média é {media}\nO maior é {maiorNumero} e o menor é {menorNumero}.")