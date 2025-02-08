class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def mudar_nome(self, novo_nome):
        self._nome = novo_nome

    def beber(self):
        if self._idade >= 18:
            print('Bebendo....')
        else:
            print('Essa pessoa não pode beber....')

    def andar(self):
        print('Andando.....')

    def falar(self):
        print('falando......')
    
    def __str__(self):
        return 'Classe Pessoa'
