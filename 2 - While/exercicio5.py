# Faça um programa que calcule a media ponderada de uma pessoa numa disciplina; para cada nota deve digitar o valor da nota e o peso dessa nota. Deve pedir as notas e pesos até que a pessoa digite -1 para a nota, que encerra o programa e mostra a média para a disciplina.

somaPeso = 0
somaNota = 0
nota = float(input("Digite a nota ou -1 para encerrar: "))

while nota != -1:
    peso = int(input("Digite o peso da prova: "))
    
    somaPeso = somaPeso + peso
    somaNota = somaNota + (nota * peso)

    nota = float(input("Digite a nota ou -1 para encerrar: "))

print(f"A média para a disciplina foi de: {somaNota/somaPeso} pontos.")
    

    




