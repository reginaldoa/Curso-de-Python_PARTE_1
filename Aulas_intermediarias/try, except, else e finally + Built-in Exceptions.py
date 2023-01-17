#try , except, else e finally


try: # Sempre começ com try, independente do que virá a seguir.
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e)
else:
    print("Não deu erro")
finally: #Sempre será executado
     print('FECHAR ARQUIVO')