#Estrutura de dados do tipo chave e valor.

# Imutaveis - str, int, float, bool, tuple
# Mutável = dict, list

# pessoa = dict(nome='Reginaldo alves')   --- Menos utilizado

pessoa = {
    'nome': "Reginaldo alves",
    'sobrenome': "Da Silva",
    'idade': 27 ,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'oie tal', 'numero': 127}
    ]
}


print(pessoa['nome'],pessoa['endereços'])
print()

for chave in pessoa:
    print(chave,pessoa[chave])