
lista_bandas = [
    ['linkin park', 'papa roach', 'green day'],
    ['fresno', 'nx zero', 'maneva'],
    ['gloria', 'evanescence', 'esteban'],
]
#print(lista[2][2]) #buscando o ultimo nome, da segunda lista

enumerada = enumerate(lista_bandas)
print(list(enumerada))

print(lista_bandas)

v1,v2,v3 = lista_bandas #Desempacotamento
print(v2)