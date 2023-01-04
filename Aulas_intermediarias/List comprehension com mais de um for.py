lista = []


for x in range(3):
    for y in range(3):
        lista.append((x,y))

lista = [
    [(x,letra) for letra  in "reginaldo"]
    for x in range(3)
]

print(lista)