#isinstance - para saber se o objeto é de determinado tipo
#Interessante para separar itens que não são uniformes e quiser iterar

lista = ['a',1,1.1,True, [0,1,2],(1,2),
            {0,1},{'nome': 'Reginaldo'},
]


for item in lista:
    if isinstance(item, set):
        print("SET")
        item.add(5)
        print(item,isinstance(item, set))

    elif isinstance(item, str):
        print("STR")
        print(item.upper(),isinstance(item, set))


    elif isinstance(item, (int, float)):
        print("NUMERO")
        print(item , item * 2)

    else:
        print("outro")
        print(item)