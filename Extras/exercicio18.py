# Crie um programa que pede números de 1 a 1000, e depois mostre quais são maiores que 500 e 
# quais são menores. A quantidade de números informados tem que ser maior ou igual a 10, 
# e menor e igual a 20.

numero = int(input("Digite um número entre 1 a 1000: "))

#numeros menores que 500
if numero < 500:
    print("Os números menores que 500 são:")
    for n in range(1, numero + 1):
        print(n)

#numeros maiores que 500
elif numero > 500:
    print("Os números maiores que 500 são:")
    for n in range(500, numero + 1):
        print(n)
