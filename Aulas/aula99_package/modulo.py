__all__ = [ #O  que tiver fora do ALL, não será importado nesse caso.
    'variavel',
    'soma',
    'teste'
]

from aula99_package.moduloB import fala_oi

variavel  = "Alguma coisa"

def soma( x , y ):
    return x + y

teste = 'teste'

fala_oi()

