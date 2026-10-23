direcoes = ["N", "L", "S", "O"]
resultados = []

with open("entrada.txt", "r", encoding="utf-8") as arquivo:
    dados = arquivo.read().split()

posicao = 0

while posicao < len(dados):
    n = int(dados[posicao])
    posicao += 1

    if n == 0:
        break

    comandos = dados[posicao]
    posicao += 1

    direcao = 0

    for comando in comandos:
        if comando == "D":
            direcao = (direcao + 1) % 4
        elif comando == "E":
            direcao = (direcao - 1) % 4

    resultados.append(direcoes[direcao])

with open("saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
    if resultados:
        arquivo.write("\n")
