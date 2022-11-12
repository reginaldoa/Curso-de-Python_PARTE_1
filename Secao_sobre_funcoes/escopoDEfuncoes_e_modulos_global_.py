#Escopo significa o local que determinado código pode atingir.

x=1

def escopo():
    global x # a palavra GLOBAL variavel do corpo externo seja manipulada no corpo interno (evitar usar)
    x = 11
    print(x)


escopo()
print(x) #o X no escopo global foi mudado, por conta da palavra "global" acima.

#CALL STACK - pilha de chamadas
