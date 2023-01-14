#Yield from 


def gen1():
    print("começou o gen1")
    yield 1
    yield 2
    yield 3
    print('acabou gen1')

def gen3():
    print("começou o gen3")
    yield 10
    yield 20
    yield 30
    print("acabou gen3")


def gen2(gen):
    print("começou o gen2")
    yield from gen() # aqui, foi chamada a função gen1, posso chamar direto na chamada também, existem mais de uma forma.
    yield 4
    yield 5
    yield 6
    print('acabou gen2')

g1 = gen2(gen1)
g2 = gen2(gen3)

for numero in g1:
    print(numero)
for numero in g2:
    print(numero)
