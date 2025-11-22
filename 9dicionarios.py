armario = {'Gaveta1' : 'Arquivo1',
           'Gaveta2' : 'Arquivo2'}

print(armario['Gaveta1']) #Arquivo1

# .get()
print(armario.get('Gaveta2')) #Arquivo2

# .keys()
print(armario.keys()) #G1 E G2

# .values()
print(armario.values()) #A1 e A2

# .items()
print(armario.items())

# .setdefault(CHAVE, VALOR)
armario.setdefault('Gaveta3','Arquivo3')
print(armario)

# .clear()
armario.clear()
print(armario)