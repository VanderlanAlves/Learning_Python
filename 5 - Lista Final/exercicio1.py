# Faça um programa que mostre o fatorial de 1 a 20. Lembrando que fatorial é a multiplicação 
# de todos os números até o indicado no fatorial. Por exemplo, 5! = 5 * 4 * 3 * 2 * 1

i = 2
fatorial = 1

for j in range(1,21):

    while i <= j:
        fatorial = fatorial * i
        i += 1

    print(fatorial)


