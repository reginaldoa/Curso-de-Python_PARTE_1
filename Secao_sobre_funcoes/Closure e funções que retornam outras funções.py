# Closure e funções que retornam outras funções


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}  {nome}'
    return saudar

    


falar_bom_dia = criar_saudacao('bom dia')
falar_boa_noite = criar_saudacao("Boa noite")
print(falar_bom_dia('Reginaldo'))
print(falar_boa_noite("Reginaldo"))


for nome in ['Reginaldo', 'Renato', 'Neide']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

