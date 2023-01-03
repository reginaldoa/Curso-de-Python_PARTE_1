import pprint

#Mapeamento de dados em list comprehension


lista = [ n for n in range(10) if n < 5]
print(lista)

numero = [teste for teste in range(100) if teste > 5 ]
print(numero) 



#O que vem na esquerda do for é mapeamento
#O que vem na direita do for é filtro

