x=5

def escopo():
    def outra_funcao():
        x=10 # esse X está no escorpo da funcao, é diferente do x que vale 5 (se quiser pode usar "global", para mudar a variavel que estava fora do escopo da função.)
        y=2
        print(x,y)

    outra_funcao()
    print(x)

escopo()
