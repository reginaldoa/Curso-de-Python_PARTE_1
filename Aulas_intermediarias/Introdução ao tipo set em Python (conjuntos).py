s1 = set() # vazio
s1 = {'Reginaldo',1,2,3} # Com dados

print(s1)

#Sets são eficientes para remover valores duplicados de iteráveis
#Os valores sempre serão únicos
s3 = {1,2,3,3,3,3,3,3,3,3,3,1}
print(1 in s3)

for numero in s3:
    print(numero)

#l1 = [1,2,3,3,3,3,3,3,3,3,3,1]
#setli = set(l1)
#transformando = list(setli)
#print(transformando)

#Os sets não garantem a ordem dos valores.
#Não aceitam valores mutáveis dentro deles.
#Não tem índexes



#Métodos úteis:
#add, update, cleat, discard

s1 = set()
s1.add("reginaldo")
s1.add(1)
s1.update(('ola mundo',1,2,3,4,5,6,7,8,9))
s1.clear() #Limpar
s1.add(1)
s1.discard(1) #Eliminar o valor que deseja descartar
print(s1)



#operadores úteis
# união | une
#Intersecção & (intersection) itens presentes em ambos
#Diferença - itens presentes apenas no set da esquerda
#Diferença simétrica ^ itens que não estão em ambos
sett =  {1,2,3}
sett2 = {3,2,0}

sett3 = sett | sett2 #União
print(sett3)

sett4 = sett & sett2
print(sett4)

sett5 = sett - sett2
print(sett5)

sett6 = sett ^ sett2
print(sett6)

#Exemplo de uso dos sets

letra = set()

while True:
    letra = input('Digite:')
    letra.add(letra.lower())

    if 'l' in letra:
        print("PARABÉNS")
        break

    print(letra)

#Poderia ser utilizado no desafio anterior, do jogo da forca, iria gastar menos espaço e tempo, melhor automatizado.
