#refatorar significa editar o código

def soma (x, y,z=None): #Após um parametro ter valor padrão, todos os próximos, irão precisar ter também.
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(100,200,0)
soma(1000,2000) #não enviei o Z, portanto, ele irá pegar o valor padrão que coloquei no parâmetro.

