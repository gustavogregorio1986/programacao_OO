from classes1 import Motocicleta, Carro, Caminhao

moto = Motocicleta('Preta', 2, 'custom')

print(moto.cor)
print(moto.qtde_rodas)
print(moto.estilo)

carro = Carro('preta', 4, 'Nissan')
caminhao = Caminhao('azul', 12, 'Scania')

print(carro.cor)
print(caminhao.acelerar())
print(carro.acelerar())

print('Polimorfismo')

lista = [1,2,3]

print(len(lista))

nome = 'Python'
print(len(nome))

for i in nome:
    print(i)


print(2 + 2)

print('a' + 'b')
