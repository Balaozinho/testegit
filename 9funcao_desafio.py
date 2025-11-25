#criar uma funcao para aplicar descontos 

def desconto (valor, desconto):
    """Usuário informa valor e desconto em absoluto"""
    resultado = valor*(1-desconto)
    return resultado

def main ():
    print (desconto(200, 0.2))

main()





