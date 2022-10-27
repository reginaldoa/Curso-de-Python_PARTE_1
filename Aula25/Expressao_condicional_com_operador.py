#utilizando o OR, ajuda a fazer condicionais simples, com uma sintaxe mais "limpa".

nome = input('Qual o seu nome? ')
print(nome or "Você não digitou nada")


a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Reginaldo'

variavel = a or b or c or d or e or f or g
print(variavel)