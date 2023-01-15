# Try, except, else e finally

try: # Tentar executar o código se ocorrer alguma exceção que não seja de sintaxe. Pula direto pro except
    a = 18
    #b = 0
    print('linha 1')
    c = a/b           # Quando ocorre o erro, vai pro except.
    print('linha 2')
except ZeroDivisionError: #SE DER OUTRO ERRO, SERÁ INFORMADO QUAL O ERRO. posso fazer vários EXCEPTs.
    print("Dividiu por zero")
except Exception:
    print("ERRO DESCONHECIDO, QUE VAI TRATAR QUALQUER OUTRO ERRO, POR CAUSA DA CLASSE 'EXCEPTION'.")

print('CONTINUA')

try:
    print(teste)
except NameError:
    print("ENTENDI")

#Exceções são erros. Em python, exceções são classes.
#Podemos pegar o nome do erro e tratar ele em especifico.