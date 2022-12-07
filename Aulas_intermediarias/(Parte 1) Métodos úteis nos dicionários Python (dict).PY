pessoa ={
    'nome': "Reginaldo",
    "sobrenome": "Alves da Silva",
    "time": "Palmeiras"
}

#Assim dá pra saber quantas chaves tem no dicionário
print(len(pessoa))

#Para retornar em outro tipo  
print(pessoa.keys())


for chave in pessoa:
    print(chave)

#Com o setdefault, caso a chave não existe e lhe seja atribuido um valor, ela virá com um valor automático
pessoa.setdefault("idade", 0)

print(pessoa)