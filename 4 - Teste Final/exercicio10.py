# Crie um programa que calcula e lista os primeiros 20 números primos.

numero = 0
mult=0

for i in range(2,21):
    if (numero % i == 0):
        mult += 1

    numero += 1    

if(mult==0):
    print(f"{numero}É primo")

