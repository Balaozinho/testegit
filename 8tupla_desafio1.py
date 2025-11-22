#EXERCICIO23 - VOCÊ É RESPONSÁVEÇ PELO CONTROLE DE UM ESTOQUE DE LOJA DE INFORMÁTICA
#CADA PRODUTO É REPRESENTADO POR UMA TUPLA COM A SEGUINTE CONFIGURAÇÃO 
#(NOME, QUANTIDADE_EM_ESTOQUE)
#MOSTRE TOS PRODUTOS COM MENOS DE 5 UNIDADES EM ESTOQUE
#MOSTRE A QUANTIDADE DE PRODUTOS ZERADOS E QUAL A QUANTIDADE TOTAL DE ITENS NO ESTOQUE

estoque = (
    ('Mouse LG Tech', 10),
    ('Mic Hyper X', 5),
    ('Acer Nitro 5', 3),
    ('Webcam HD', 0)
)

for i in estoque:
    if i[1] < 5:
        print(f" - {i[0]} tem {i[1]} qtdades!")

#qtdade produtos zeros
soma_zerada = 0
for i in estoque:
    if i[1] == 0:
        soma_zerada += 1

print(f'A qtdade de itens zerados é de: {soma_zerada}')

#qtdade de itens 
soma_total = 0
for i in estoque:
    soma_total += i[1]

print(f'A qtdade total de produtos: {soma_total}')
