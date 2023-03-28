#Escopo da classe e de métodos da classe

class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel= 'valor'
        print(variavel)

    def acao(self, alimento):
        return f"{self.nome} e um animal muito bonito! EstA comendo {alimento}"
    

    def Executar(self, *args, **kwargs):
        return self.acao( *args, **kwargs)

        #Qualquer método do self, tem acesso a tudo o que estiver na classe  



leao = Animal(nome = 'leao')
print(leao.nome) 
print(leao.Executar("banana"))