#Exercício respondido, antes de ver a resolução durante a aula
#Exercício - sistema de perguntas e respostas

perguntas = [{
    'pergunta': 'Quanto e 2+2?',
    'opcoes': ['1','2','3','4'],
    'Resposta': '4'
},{
    'pergunta': 'Quanto e 5*5?',
    'opcoes': ['25','55','10','51'],
    'Resposta': '25'
},{
    'pergunta': 'Quanto e 10/2?',
    'opcoes': ['4','5','2','1'],
    'Resposta': '5'
}]

#Já consegui resolver a lógica, agora vou verificar como o professor fez para ficar com os detalhes que não são de lógica.


acertou = 0
for pergunta in perguntas:
    print('Pergunta:',pergunta["pergunta"])

    for i, opcao in enumerate(pergunta['opcoes']):
        print(f'{i})',opcao)

    minha_resposta = input("Escolha uma opção:")
    if minha_resposta == pergunta['Resposta']:
        acertou +=1
        print(f'Resposta certa!')
        print()
    else:
        print("Resposta errada!")
        print()

if acertou == 3:
    print(f"Parabéns, você acertou {acertou}/3!!!!")

elif acertou == 2:
    print(f"Você acertou {acertou}/3, ainda pode melhorar.")

elif acertou == 0 or 1:
    print(f"Você acertou {acertou}/3, precisa melhorar.")

