"""
 args - argumentos não nomeados
*args - (empacotamento e desempacotamentos)
"""

def soma(*testando):
    total = 0
    for numero in testando:
        total += numero
    return total

somando = soma(1,2,3)
print(somando)


numeros = 5, 5

somando2 = soma(*numeros)
print(somando2)

print(sum((10,10))) #com o sum, se torna mais fácil de somar números sem fazer uma função, como a de cima, por exemplo.


print(sum(numeros))