#Desafio feito, antes de olhar a aula da resolução.
'''
 for / while
  0 10
  1  9
  2  8
  3  7
  4  6
  5  5
  6  4
  7  3
  8  2
'''


contador = 0
reduzindo = 10

while reduzindo >= 2: #Dessa forma deu certo.
    print(contador,reduzindo)
    contador += 1
    reduzindo -= 1


#Resolução do professor

for p, r in enumerate(range(10 , 1 , -1)):
    print(p,r)