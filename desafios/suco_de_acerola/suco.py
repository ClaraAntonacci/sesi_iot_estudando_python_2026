resultados = []

with open("entrada.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    valores = linha.split()

    if len(valores) < 2:
        continue

    amigos = int(valores[0])
    frutas = int(valores[1])

    if amigos == 0 and frutas == 0:
        break

    volume_litros = (frutas * 50) / 1000 / amigos
    resultados.append(f"{volume_litros:.2f}")

with open("saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
    if resultados:
        arquivo.write("\n")
