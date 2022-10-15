#Crie um programa que peca as 4 notas da avaliação de um estudante e verifique se ele foi aprovado.
#Cada avaliação vale no mínimo 0 e no máximo 10. As notas podem ser decimais, por exemplo 7.5.
#Para ser aprovado ele precisa ter média igual ou maior que 7 e não ter tirado 0 em nenhuma prova.
#No final, mostre as 4 notas, a média, se o aluno foi aprovado e, caso não tenha sido aprovado, mostre porque.

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

if (0<nota1<10) and (0<nota2<10) and (0<nota3<10) and (0<nota4<10):

    media = (nota1 + nota2 + nota3 + nota4)/4

    if media >= 7:
        print(f"Você foi aprovado com média {media:.02f}! Você tirou {nota1} na primeira prova, {nota2} na segunda prova, {nota3} na terceira prova e {nota4} na quarta prova.")

    else:
        print(f"Você não foi aprovado pois sua média de {media:.02f} pontos não atingiu a média 7.")    

else:
    print("Nota inválida!")


