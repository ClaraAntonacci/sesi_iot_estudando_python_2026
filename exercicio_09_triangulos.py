
# Programa que classifica um triângulo.

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Os lados devem ser positivos.")
elif (lado1 + lado2 <= lado3 or
      lado1 + lado3 <= lado2 or
      lado2 + lado3 <= lado1):
    print("Esses lados não formam um triângulo.")
elif lado1 == lado2 and lado2 == lado3:
    print("Triângulo equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")

