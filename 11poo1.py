#criarmos uma classe (molde)
class Carro:
    def __init__ (self, modelo, cor): #definimos os atributos
        self.modelo = modelo
        self.cor = cor

    def acelerar(self): #definimos seus métodos/comportamentos
        print(f'O {self.modelo} está acelerando!')

#Criar o objeto
meu_carro = Carro ('fiat', 'preta')

#Acessar seus atributos e métodos
print(meu_carro.modelo) #fiat
print(meu_carro.cor)

meu_carro.acelerar()