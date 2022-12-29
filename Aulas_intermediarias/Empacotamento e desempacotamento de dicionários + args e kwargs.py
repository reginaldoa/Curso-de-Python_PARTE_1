#Empacotamento e desempacotamento de dicionários

#args e kwargs
#Kwargs - keyword argumentos (argumentos nomeados)


a, b = 1 ,2 
a,b = b, a 
#print(a,b)


pessoa = {
    'nome':'Reginaldo',
    'sobrenome':'Alves'
}
(a1,a2), (b1, b2) = pessoa.items()
print(a1,a2)
print(b1,b2)


for chave  , valor in pessoa.items():
    print(chave , valor)



print("############################################")
print()
print()
print()
print()
print()
print()



pessoa1 = {
    'nome':'Reginaldo',
    'sobrenome':'Alves'
}
(a1,a2), (b1, b2) = pessoa.items()
print(a1,a2)
print(b1,b2)



dados_pessoa = {
    'idade' : 27,
    'altura': 1.76
}



pessoas_completa = {**pessoa, **dados_pessoa}

print(pessoas_completa)
print()
print()
print()
print()
print()
print()



#args e kwargs
#args (já vimos)
#Kwargs - keyword argumentos (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs): #kwargs sempre sao dois asteriscos 
    print("não noemados:" , args)
    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(1,2 ,nome='teste', idade= 123456)
mostro_argumentos_nomeados(**pessoas_completa)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)


print()
print()
print()
print()
print()
print()




eu = {
    'sou':"reginaldo",
    'tenho': 27
}



def teste(*args, **kwargs):
    print(*args)
    for valor, chave in kwargs.items():
        print(valor, chave)



teste('pessoa', eu)