#Uma sequência de números famosa é a chamada sequência de Fibonnaci.

# Ela funciona assim:

# O primeiro e segundo números são o 1.
# O terceiro é o primeiro somado do segundo (1 + 1 = 2, o terceiro é o 2)
# O quarto é o segundo acrescido do terceiro (1 + 2 = 3, o quarto é o 3)
# Por aí vai...
# Assim, um número é sempre a soma dos dois números que vêm antes dele.

# Escreva um código que mostre na tela ("print") o 13º número da sequência de Fibonacci.

lista_fibonnaci = [1, 1]
limite_lista = 13
numero =  0

for i in range(2, limite_lista):
    numero = lista_fibonnaci[i - 1] + lista_fibonnaci[i - 2]

    lista_fibonnaci.append(numero)

print(lista_fibonnaci[-1])
