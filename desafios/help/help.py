resultados = []

with open("entrada.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

posicao = 0

while posicao < len(linhas):
    linha = linhas[posicao].strip()
    posicao += 1

    if not linha:
        continue

    n = int(linha)

    if n == 0:
        break

    erros = {}
    tempo_total = 0
    problemas_resolvidos = 0

    for _ in range(n):
        problema, tempo_texto, julgamento = linhas[posicao].split()
        posicao += 1
        tempo = int(tempo_texto)

        if julgamento == "incorrect":
            erros[problema] = erros.get(problema, 0) + 1
        elif julgamento == "correct":
            problemas_resolvidos += 1
            tempo_total += tempo
            tempo_total += erros.get(problema, 0) * 20

    resultados.append(f"{problemas_resolvidos} {tempo_total}")

with open("saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
    if resultados:
        arquivo.write("\n")
