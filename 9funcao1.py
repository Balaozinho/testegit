import random

#SEM PARAM E SEM RETORNO 
def bemvindo ():
    print("Seja muito bem-vindo")

bemvindo()
bemvindo()
bemvindo()

#SEM PARAM E COM RETORNO
def aleatorio_1_100 ():
    return random.randint(1,100)

print(aleatorio_1_100())
print(aleatorio_1_100())

#COM PARAM E SEM RETORNO
def bemvindo_personalizado (nome):
    print(f'Seja muito bem-vindo {nome}')

bemvindo_personalizado('Alvaro')
bemvindo_personalizado('Leticia')

#COM PARAM E COM RETORNO
def soma3_mult10 (numero):
    """Soma 3 e multiplica por 10 um número informado"""
    resultado = (numero + 3)*10
    return resultado

print(soma3_mult10(2)) #50
