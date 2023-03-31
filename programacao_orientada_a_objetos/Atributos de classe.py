# Atributo de classe


class Pessoa:
    ano_atual = 2023


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    


p1 = Pessoa("Reginaldo", 27)
print(Pessoa.ano_atual)
Pessoa.ano_atual = 1
Pessoa.ano_atual = 2023
print(p1.get_ano_nascimento())