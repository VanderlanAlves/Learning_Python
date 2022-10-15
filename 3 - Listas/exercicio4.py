#Peça dois numeros ao usuario, e retorne a soma, subtração, divisão, mutiplicação e potenciação dos dois números.
#Mostre todos os resultados no formato com 4 casas decimais.

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1/numero2
potenciacao = numero1**numero2

print(f"{soma:.04f}")
print(f"{subtracao:.04f}")
print(f"{multiplicacao:.04f}")
print(f"{divisao:.04f}")
print(f"{potenciacao:.04f}")