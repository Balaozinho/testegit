#calcular média de um aluno
notas = [9,7,4,8]
media = sum(notas) / len(notas)
print(f'A média do aluno é de: {media}')

#Olá customizado
nomes = ["Ana", "Alvaro", "Leticia"]
for n in nomes:
    print(f"Seja muito bem-vindo(a) {n}")

#filtro de nomes com J
alunos = ["Ana", "João", "Jair", "Felipe"]
alunos_J = []

for a in alunos:
    if a.startswith("J"):
        alunos_J.append(a)

print(alunos_J)