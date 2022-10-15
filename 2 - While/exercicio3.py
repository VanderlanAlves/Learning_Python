# Faça um programa que recebe um número e mostre todos os divisiveis por ele de 1 ate ele.

numero = int(input("Digite um número inteiro: "))
i = 0

while i != numero:
    i = i + 1
    if numero % i == 0:
        print(f"O {numero} é divisível por {i}.")
    else:
        print(f"O {numero} não é divisível por {i}.")
    
    