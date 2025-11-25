#criarmos uma classe (molde)
class Carro:
    def __init__ (self, modelo, cor): #definimos os atributos
        self.modelo = modelo
        self.cor = cor

    def acelerar(self): #definimos seus métodos/comportamentos
        print(f'O {self.modelo} está acelerando!')

#Classe filha (herde os atributos e métodos da classe mãe)
class carro_conversivel (Carro):
    def recuar_teto(self):
        print(f'O teto do {self.modelo} está recuando!')

#Criar o objeto
Carro_Convers = carro_conversivel('BMW', 'Preta')

#Acessando métodos e atributos
Carro_Convers.recuar_teto()