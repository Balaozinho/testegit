#EXERCICIO 21 - SISTEMA DE ANÁLISE DE DESEMPENHO DE ARENAS
#VOCÊ TEM 3 PLAYERS QUE JOGARAM EM 5 ARENAS, APURANDO SUAS PONTUAÇÕES NA LISTA ARENAS
#SUA FUNÇÃO É CALCULAR A MÉDIA DE PONTOS DE CADA PLAYER
#ARMAZENAR AS MÉDIAS EM UMA NOVA LISTA
#IDENTIFICAR QUAL JOGADOR TEVE A MELHOR MÉDIA DE TODAS AS ARENAS JOGADAS
#DICAS: UTILIZE FOR, ENUMERATE, MÉTODOS DE LISTAS COMO O SUM, LEN, APPEND E INDEX
#MOSTRE TODOS OS RESULTADOS EM TELA

arenas = [
    [1200, 1500, 1100, 1800, 1700],
    [1000, 950, 1100, 1050, 980],
    [2000, 1900, 1950, 2100, 2200],
]

medias_jogadores = []

for j in arenas:
    media = sum(j) / len (j)
    print(f'A média é de: {media}')
    medias_jogadores.append(media)

print(medias_jogadores)

#JOGADOR COM A MAIOR MEDIA
melhor_desempenho = medias_jogadores.index(max(medias_jogadores))
print(f"O jogador com a melhor média é o Player: {melhor_desempenho + 1}")

