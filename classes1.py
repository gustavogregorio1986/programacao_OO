class Veiculo:
    def __init__(self, cor: str, qtde_rodas: int) -> None:
        self._cor = cor
        self._qtde_rodas = qtde_rodas

    @property
    def cor(self):
        return self._cor
    
    @property
    def qtde_rodas(self):
        return self._qtde_rodas
    
    def alerta(self):
        return 'Aleta da classe pai'
    
class Motocicleta(Veiculo):
    def __init__(self, cor, qtde_rodas, estilo: str):
        super().__init__(cor, qtde_rodas)
        self._estilo = estilo

    @property
    def estilo(self):
        return self._estilo
    
    def acelera(self):
        return 'Acelerar motociclta'
    
    def alerta(self):
        return super().alerta()
    
class Carro(Veiculo):
    def __init__(self, cor: str, qtde_rodas: int, marca: str) -> None:
        super().__init__(cor, qtde_rodas)
        self._marca = marca

    @property
    def marca(self):
        return self._marca

    def acelerar(self):
        return 'Acelerando o carro.....'
    
class Caminhao(Veiculo):
    def __init__(self, cor, qtde_rodas, montadora: str):
        super().__init__(cor, qtde_rodas)
        self._motadora = montadora

    @property
    def montadora(self):
        return self._motadora
    
    def acelerar(self):
        return 'Acelerando o carro.....'
    
    def acelerar(self):
        return 'Acelerando o caminhão.....'