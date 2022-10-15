# Crie um conjunto de funções que calculem:

# a área de um retângulo
# a área de um triangulo
# a área de circulo
# o comprimento de um retângulo
# o comprimento de um triangulo
# o comprimento de circulo
# Crie depois dois exemplos de uso de cada função

#AreaTriangulo
baseTriangulo = float(input("Digite o valor da base do triângulo: "))
alturaTriangulo = float(input("Digite o valor da altura do triângulo: "))

def calcular_area_triangulo(baseTriangulo, alturaTriangulo):
    areaTriangulo = (baseTriangulo * alturaTriangulo)/2

    return areaTriangulo

print(calcular_area_triangulo(baseTriangulo,alturaTriangulo))

#AreaRetangulo
baseRetangulo = float(input("Digite o valor da base do Retangulo: "))
alturaRetangulo = float(input("Digite o valor da altura do Retangulo: "))

def calcular_area_retangulo(baseRetangulo, alturaRetangulo):
    areaRetangulo = baseRetangulo * alturaRetangulo

    return areaRetangulo

print(calcular_area_retangulo(baseRetangulo,alturaRetangulo))

#AreaCirculo
valorDePi = 3.14
raioCirculo = float(input("Digite o valor do raio do Circulo: "))

def calcular_area_circulo(valorDePi, raioCirculo):
    areaCirculo = valorDePi * (raioCirculo**2)

    return areaCirculo

print(calcular_area_circulo(valorDePi,raioCirculo))

#ComprimentoRetangulo
baseRetangulo = float(input("Digite o valor da base do Retangulo: "))
alturaRetangulo = float(input("Digite o valor da altura do Retangulo: "))

def calcular_comprimento_retangulo(baseRetangulo, alturaRetangulo):
    comprimentoRetangulo = (baseRetangulo * 2) + (alturaRetangulo * 2)

    return comprimentoRetangulo

print(calcular_comprimento_retangulo(baseRetangulo,alturaRetangulo))

#Comprimento de um triangulo:
cateto1 = float(input("Digite o valor do cateto 1 do triângulo: "))
cateto2 = float(input("Digite o valor do cateto 2 do triângulo: "))
cateto3 = float(input("Digite o valor do cateto 3 do triângulo: "))

def calcular_comprimento_triangulo(hipotenusa, cateto1, cateto2):
    comprimentoTriangulo = hipotenusa + cateto1 + cateto2

    return comprimentoTriangulo

print(calcular_comprimento_triangulo(cateto1, cateto2, cateto3))


# o comprimento de circulo
valorDePi = 3.14
raio = float(input("Digite o valor do raio do circulo: "))

def calcular_comprimento_circulo(valorDePi, raio):
    comprimentoCirculo = 2 * valorDePi * raio

    return comprimentoCirculo

print(calcular_comprimento_circulo(valorDePi, raio))

# Crie depois dois exemplos de uso de cada função

#Exemplo 1
raio = 30
print(calcular_comprimento_circulo(valorDePi, raio))

#Exemplo 2
baseRetangulo = 30
alturaRetangulo = 15

print(calcular_area_retangulo(baseRetangulo,alturaRetangulo))