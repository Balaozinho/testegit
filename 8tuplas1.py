#criar lista de vestuário
loja1 = ['Camiseta', 'Shorts', 'Vestido']
loja1[0] = "Camisa"

print(loja1)

loja2 = ('Camiseta', 'Shorts', 'Vestido')
#loja2[0] = 'Camisa'

loja3 = ('Camiseta', 'Shorts', 'Vestido', 'Vestido', 'Camiseta')

# .count()
print(loja3.count('Vestido')) #2

# .index()
print(loja3.index('Vestido')) #2