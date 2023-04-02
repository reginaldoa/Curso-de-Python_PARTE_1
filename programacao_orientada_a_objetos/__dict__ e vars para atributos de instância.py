# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    


p1 = Pessoa('Reginaldo', 27)
#del p1.nome    - se quiser apagar 

print(p1.__dict__) # Retorna os valores
print(vars(p1)) # Também retorna os valores