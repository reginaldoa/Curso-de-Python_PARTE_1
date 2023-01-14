#Introdução a generator functions em Python
# Generator = (n for n in range(1000000)) 
# O generator é uma função que dá pra pausar

def generator( n= 0 , maximun = 10):
   while True:
        yield n # yeld Pausa a função
        
        n += 1


        if n > maximun:
            return 

        

gen = generator(maximun= 1000)

for n in gen:
    print(n)