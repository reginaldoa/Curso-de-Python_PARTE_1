"""
 args - argumentos não nomeados
*args - (empacotamento e desempacotamentos)
"""

x, y, *resto = 1,2,3,4
print(x,y,resto)

def soma(x,y):
    return x + y

print(1, 2, 3, 4, 5)


def teste(*testando):
    total = 0
    for numero in testando:
        total = total + numero
        print(f"{total}")

teste(1,2,3,4,5,6)