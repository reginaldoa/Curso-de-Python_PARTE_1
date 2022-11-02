def funcao(var):
    return var
    #Nada será executado depois do return

variavel = funcao("valor que eu quero")

if variavel:
    print(variavel)
else:
    print("nenhum valor")



def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

conta = divisao(51,5)

if conta:
    print(conta)
else:
    print('invalida')


def dumb():
    return ('Reginaldo' , 'Alves')

var = dumb()

print(var[1] , type(var))