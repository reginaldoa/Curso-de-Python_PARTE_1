# Resolvi os exercícios, antes de ver a resolução na aula.


#Crie uma função que multiplica todos os argumentos não nomeados 
#Retorne  o total para uma variável e mostre o valor da variavel

#Crie uma função fala se um número é par ou ímpar.
#Retorne se esse número é par ou ímpar

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
        

resultado = multiplica(1,2,3,4,5)
print(resultado)


def par_impar(x):
    if x ==0:
        return "Informe um numero que nao seja zero"
    elif x % 2 == 0:
        return f"O numero {x} e par"
    else :
        return f"O numero {x} e impar"

par_ou_impar = par_impar(7)
print(par_ou_impar)