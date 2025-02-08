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
    
class Motocicleta(Veiculo):
    def __init__(self, cor, qtde_rodas, estilo: str):
        super().__init__(cor, qtde_rodas)
        self._estilo = estilo

    @property
    def estilo(self):
        return self._estilo
    
    def acelera(self):
        return 'Acelerar'
