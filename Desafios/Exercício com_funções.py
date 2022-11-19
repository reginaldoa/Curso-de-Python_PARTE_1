#Crie funções que duplicam, triplicam e quadriplicam o número recebido como parâmetro

"""""
Forma mais simples
def multiplica(numero):
    return numero *2

def triplica(numero):
    return numero *3

def quadriplicam(numero):
    return numero *4


dois   = multiplica(5)
tres   = triplica(5)
quatro =  quadriplicam(5)

print(dois)
print(tres)
print(quatro)

"""


#Forma mais complexa, porém, deixa o código mais limpo

def criar_multiplicador(multiplicar):
    def multiplicando(numero):
        return numero * multiplicar
    return multiplicando


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(duplicar(5))
print(triplicar(5))