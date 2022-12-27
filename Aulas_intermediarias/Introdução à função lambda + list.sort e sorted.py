#A função lambda é anônima, contém apenas uma linha.

lista = [4,32,1,34,5,6,6,21, ]

lista.sort() # Ordenando a lista
print(lista)

lista.sort(reverse= True) # Ordem reversa
print(lista)

#Sorted() é a mesma coisa que sort()


pessoa = [
    {'nome': 'Deginaldo', 'sobrenome': 'Alves da Silva'},
    {'nome': 'Beginaldo', 'sobrenome': 'Alves da Silva'},
    {'nome': 'Aeginaldo', 'sobrenome': 'Alves da Silva'},
    {'nome': 'Ceginaldo', 'sobrenome': 'Alves da Silva'}

]


def exibir(lista):
    for item in lista:
        print(item)

L1 = sorted(pessoa, key=lambda item: item ['nome'])
L2 = sorted(pessoa, key=lambda item: item ['sobrenome'])


exibir(L1)
exibir(L2)