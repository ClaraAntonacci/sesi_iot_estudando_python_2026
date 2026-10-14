
# Programa que calcula o fatorial de um número.

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("Digite um número não negativo.")
else:
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial = fatorial * i

    print("O fatorial de", numero, "é:", fatorial)
