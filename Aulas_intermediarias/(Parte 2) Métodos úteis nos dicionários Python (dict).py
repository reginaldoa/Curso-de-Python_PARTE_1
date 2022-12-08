p1 = {
    'nome':"Reginaldo",
    'sobrenome': 'Alves'
}

#Se o 'nome' não existisse, iria setar um valor, nesse caso o None
print(p1.get('nome', None))

#Com o pop, elimina a chave escolhida, porém, podemos guardar o valor em uma variavel, como no exemplo abaixo.
nome = p1.pop('nome')
print(nome)
print(p1)

print("###########################")

#Elimina a última chave
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

#Atualiza chaves, cria chaves, etc.
p1.update({
    'nome': 'NOVO VALOR',
    'idade': 27

})

p1.update(nome='OUTRO VALOR', idade= 28)
print(p1)

print("#########################")

tupla = ('nome','novo valor'), ('idade',28)
p1.update(tupla)

print(p1)

lista = [['nome','palmeirense'], ['idade',27]]
p1.update(lista)
print(p1)