produto = {
    'nome':'caneta azul',
    'preco': 2.5,
    'categoria':'Escritorio',
}




dc = {
    chave: valor
    if isinstance(valor, (int ,float)) else valor.upper()
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}


lista = [
    ('a', 'valor a '),
    ('b', 'valor a '),
    ('c', 'valor a '),
    ('d', 'valor a '),
]

dc2 = {
    chave: valor
    for chave, valor in lista
}

print(dc2)
print(dict(lista))

#s1 = {i for i in range(10)}
print(set(range(10)))
print(range(10))