#Funções de primeira classe

#Podem ser tratadas como qualquer outro tipo de dado


def saudacao(msg, nome):
    return f'{msg},{nome}!' 


def executa(funcao,*args):
    return funcao(*args)


v = executa(saudacao,'oi','reginaldo')
print(v)



def teste1(nome):
    return nome


def teste2(funcao):
    return funcao

testando = teste2(teste1("reginaldo"))
print(testando)