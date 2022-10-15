#Crie um programa que calcule e mostre o salário de uma pessoa baseado no valor/hora do trabalho e na quantidade de horas trabalhadas, e na quantidade de dias trabalhados.

valor_hora_trabalho = float(input("Digite o valor da hora-trabalho: "))
qtd_horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas por dia: "))
qtd_dias_trabalhados = int(input("Digite a quantidade de dias trabalhados: "))

salario_bruto = valor_hora_trabalho * qtd_horas_trabalhadas * qtd_dias_trabalhados

porcentagem_INSS = 8
desconto_INSS = salario_bruto * (porcentagem_INSS / 100)

salario_liquido = salario_bruto - desconto_INSS

print(f"Seu salário bruto é R${salario_bruto:.02f} e seu salario após os descontos é R${salario_liquido:.02f}")

