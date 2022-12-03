pessoa = {}

pessoa['nome'] = 'Reginaldo'
pessoa['sobrenome'] ="alves da silva"
pessoa['idade'] = 27

chave = 'nome_completo'

pessoa[chave] = "neide alves"
lista =[]

del pessoa['sobrenome']

print(pessoa[chave])
print(pessoa)


time ={}

time["torcedor"] = 'palmeiras'
time["ultimo_titulo"] ="brasileiro"

chave2 = "maior_rival"
time[chave2] ="corinthians"

#Se deletar a chave, e tentar chamar a mesma depois, vai dar erro.
del time[chave2]

if time.get('chave2', None) is None:
    print('NAO EXISTE')
else:
    print(time[chave2])


