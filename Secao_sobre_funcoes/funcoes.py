# Funções - def em Python (parte 1)
#A função evita a repetição das mesmas coisas no código.

def funcao(msg): #parametro
    print(msg)
funcao('ola')

def conta (numero1,numero2):
    print(numero1 + numero2)
conta(5,5)

def saudacao(nome, sobrenome):
    print(f'Olá {nome.replace("e","8")}, seu sobrenome é {sobrenome}')
saudacao(sobrenome='Reginaldo',nome='Alves') #Consigo inverter os valores dessa forma, caso contrário, vai seguir a ordem correta.




