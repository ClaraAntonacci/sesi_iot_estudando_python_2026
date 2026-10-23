with open("entrada.txt", "r", encoding="utf-8") as arquivo:
    dados = arquivo.read().split()

resultados = []

for valor in dados:
    n = int(valor)

    if n == 0:
        break

    portas_abertas = []
    numero = 1

    while numero * numero <= n:
        portas_abertas.append(str(numero * numero))
        numero += 1

    resultados.append(" ".join(portas_abertas))

with open("saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
    if resultados:
        arquivo.write("\n")
