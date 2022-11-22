#Exemplo de funções interligadas na outra.
def nome(n):
    def sobrenome(s):
        return f'ola {n} {s}, tudo bem?'
    return sobrenome


saudacao = nome('Reginaldo')
print(saudacao('Alves'))
