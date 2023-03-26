#Métodos em instâncias de classes em Python 
#Hard coded = É  algo que foi escrito diretamente no código
#Método é uma função que está dentro da classe, o primeiro parametro é "self", ou seja, a instância em si.

class Carro:
    def __init__(self, nome = 'Sei la'):
        self.nome = nome

    def Acelerar(self):
        print(f'O carro {self.nome} esta acelerando')

fusca= Carro('Fusca')
print(fusca.nome)
fusca.Acelerar()

celta = Carro("celta")
print(celta.nome)
celta.Acelerar()



#Teste
class Time:
    def __init__(self, apelido):
        self.apelido = apelido

    def campeao(self):
        print(f'{self.apelido} e campeao!!!')


palmeiras = Time("Verdao")
print(palmeiras.apelido)
palmeiras.campeao()

selecao_brasileira = Time("Penta campeao da Copa do Mundo")
print(selecao_brasileira.apelido)
selecao_brasileira.campeao()