lista_frutas = ["Banana", "Maçã", "Uva"]

#Método .append
lista_frutas.append("Kiwi")
print(lista_frutas)

#Método .insert(posi, elemento)
lista_frutas.insert(1, "Melancia")
print(lista_frutas)

#Método .remove()
lista_frutas.remove("Banana")
print(lista_frutas)


lista_numeros = [2, 5, 6, 2, 2, 4, 1]
#método .sort()
lista_numeros.sort()
print(lista_numeros)

lista_numeros.sort(reverse=True)
print(lista_numeros)

# .reverse()

lista_numeros2 = [2, 5, 6, 2, 2, 4, 1]
lista_numeros2.reverse()
print(lista_numeros2)

# .count()
print(f'Ocorrências do número 2: {lista_numeros2.count(2)}')

# len(LISTA)
print(f"TAMANHO DA LISTA NUMEROS_2: {len(lista_numeros2)}")

# .index(valor)
print(f'Posição da primeira ocorrência do número 4: {lista_numeros2.index(4)}')