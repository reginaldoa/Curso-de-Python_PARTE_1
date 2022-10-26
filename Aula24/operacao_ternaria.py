#Muito parecido com os ifs e elses tradicionais.

logged_user = True
msg = "Usuário logado." if logged_user else "Usuário precisa fazer login"

print(msg)

idade = input("Qual é a sua idade?")

if not idade.isnumeric():
    print("É necessário informar apenas números para validar a idade.")
else:
    idade = int(idade)
    bebidas = "Você pode beber" if idade >= 18 else "Você não pode beber"

    print(bebidas)