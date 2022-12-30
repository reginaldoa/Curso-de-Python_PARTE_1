#Lista comprehension em Python
#List comprehension é uma forma rápida para criar listas
#a partir de iteráveis


#print(list(range(11)))

lista = []

#for numero in range(10):
 #   lista.append(numero)
#print(lista)


#é uma forma mais rápida de usar um FOR
lista = [
    numero * 2
    for numero in range(10)
]
print(lista)