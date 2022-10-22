'''
Slip, Join, Enumerate em Python

*Slip - DIVIDIR UMA STRING
*Join - JUNTAR UMA LISTA
*Enumerate - ENUMERAR ELEMENTOS DA LISTA # ITERAVEIS
'''

string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

#print(lista_1)
#print(lista_2)

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor) # o count vai contar quantas vezes determinada palavra apareceu na string.

    if qtd_vezes > contagem: #caso as palavras apareçam a mesma quantidade de vezes, irá considerar a que apareceu primeiro.
        contagem = qtd_vezes
        palavra = valor

print(f' A palavra que apareceu mais vezes foi "{palavra}", ela apareceu {contagem} vezes')


for valor in lista_2:
    print(valor.strip().capitalize()) #strip tira os espaços do começo e fim, o capitalize deixa a primeira letra maiuscula.


#FUNÇÃO JOIN - TRANSFORMA A STRING EM UMA LISTA

string_join = 'O palmeiras é tri.'
lista_join = string_join.split(' ')
string_join2 = ','.join(lista_join)

print(string_join)
print(lista_join)
print(string_join2)


#Enumerate - enumera elementos de uma lista

lt = "o Brasil é penta."
for indice, valor in enumerate(lt):
    print(indice, lt[indice])


uma_lista = [
    [1,'reginaldo'],
    [3,'alves'],
    [5,'da silva']
]

for indice, v in enumerate(uma_lista):
    print(indice, v[1])


#o Enumerate retorna tuplas (ver posteriormente)


n0, n1, n2 = uma_lista #desempacotamento de variaveis (ver posteriormente)

print(n2)