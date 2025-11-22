notas = [
    ["Ana", [8,7,9]],
    ["Carlos", [5,6,7]],
    ["João", [10,9,8]],
]

#CALCULAR MÉDIA POR ALUNO DA LISTA
for a in notas:
    nome_aluno = a[0]
    media = sum(a[1]) / len(a[1])
    print(f'Nome: {nome_aluno} | Média: {media}')