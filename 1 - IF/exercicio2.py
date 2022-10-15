#Faça um programa que peça 4 numeros, x, y, z e w, e calcule x elevado a y, e z elevado a w; depois mostre os dois resultados e qual é o maior

w = float(input("Um número para ser W: "))
x = float(input("Um número para ser X: "))
y = float(input("Um número para ser Y: "))
z = float(input("Um número para ser Z: "))

a = x**y
b = z**w

print(f"{x} elevado a {y} é igual a {a:.02f}")
print(f"{z} elevado a {w} é igual a {b:.02f}")

if a > b:
    print(f"{a} é o maior")

elif a < b:
    print(f"{b} é o maior")

else:
    print(f"Os valores são iguais.")



