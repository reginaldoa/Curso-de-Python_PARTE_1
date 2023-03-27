#Entendendo self em classes python.
#Classe - Molde (geralmente sem dados).
#Instancia da class ( objeto) - tem os dados.
#Uma classe pode gerar várias intâncias.
#Na classe o self é a própria instância.

class Car:
    def __init__(self, nome):
        self.nome = nome


    def Acelerar(self):
        print(f'{self.nome} esta  acelerando')


fusca = Car("Fusca")
print(fusca.nome) 
Car.Acelerar(fusca)