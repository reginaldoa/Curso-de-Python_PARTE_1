#São considerados falsos
#Mutáveis [] {} set()
#Imutáveis () "" 0 0.0 None False range(0,10)

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ""
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsos(valor):
    if valor == False:
        print("False")
    else:
        print("Verdadeiro")

#Qualquer coisa fora disso, teoricamente seria considerado verdadeiro, pelo menos até esse momento do curso.

def falsy(valor):
    return "Falsy" if not valor else "truthy"


print(f'teste', falsy("teste"))
print(falsy(lista))
print(falsy(dicionario))
print(falsy(conjunto))
print(falsy(tupla))
print(falsy(string))
print(falsy(inteito))
print(falsy(flutuante))
print(falsy(nada))
print(falsy(falso))
print(falsy(intervalo))

