# Faça um programa que recebe um número e mostra uma lista de todos os número pares até o número 
# informado, CONSIDERANDO o número informado.

numero = int(input("Digite um número: "))

for n in range(1, numero + 1):
    if n % 2 == 0:
        print(f"O número {n} é par.")


