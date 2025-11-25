#criando a classe mãe
class Animal:

    def emitir_som(self):
        print(f'Som genérico de um animal')

#criar subclasses (classes filhas)
class cachorro (Animal):

    def emitir_som(self):
        print(f'AU AU')

class gato (Animal):

    def emitir_som(self):
        print(f'MIAU')

#criando o objeto cachorro e gato
billy = cachorro()
filomena = gato ()

#acessar os métodos reescritos
billy.emitir_som()
filomena.emitir_som()

