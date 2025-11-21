frase = "O PythOn É MaiS LegaL"

# .capitalize()
print(frase.capitalize())

# .title()
print(frase.title())

# .center (TAMANHO, CARACTERE)
print(frase.center(50, '-'))

# len (OBJETO)
print(len(frase))

# .upper()
print(frase.upper())

# .lower()
print(frase.lower())

# .find(PALAVRA)
print(frase.find('P'))

# .replace(PALAVRA ANTIGA, PALAVRA NOVA)
print(frase.replace('PythOn', 'One Piece'))


arquivo = 'cadastro_clientes.txt'
print(arquivo.startswith('cadastro'))
print(arquivo.endswith('.csv'))

# .isalpha()
print("Python".isalpha()) #True #False

# .isdigit()
print("Python123".isdigit())

# .isalnum()
print("Python123".isalnum()) #True

# .strip()
senha = '   123456 '
if senha.strip() == '123456 ':
    print("Deu tudo certo!")
else:
    print("Deu ruim! Tente de novo!")