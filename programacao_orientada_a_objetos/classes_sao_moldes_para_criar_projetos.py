#Str é uma classe
#As classes geram novos objetos (ou instancias)

string = 'Reginaldo'
print(string.upper())
print(isinstance(string, str))

class Pessoa:
    ...


p1 = Pessoa()
p1.nome = "Reginaldo"
p1.sobrenome = "Alves da Silva"
print(p1.nome)
print(p1.sobrenome)  #Atributos, sempre procurar sem os parenteses 

p2 = Pessoa()
p2.nome = "Tauros"
p2.sobrenome = "Alves da Silva"
print(p2.nome)
print(p2.sobrenome)  #Atributos, sempre procurar sem os parenteses 


class time:
    ...

time.torcida = "Palmeiras"
print(time.torcida)

