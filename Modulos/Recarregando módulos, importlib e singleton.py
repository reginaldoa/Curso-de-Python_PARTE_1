#Singleton = só carrega o módulo uma vez no programa.

import importlib 

import testesmod

print(testesmod.variavel_modulo)


for i in range(10):
    #print(i)
    importlib.reload(testesmod) #com o importlib e reload, dá pra recarregar todo o módulo mais de uma vez.
    #Não é comum, mas pode acontecer. 
    # O comportamento padrão é carregar apenas uma vez.

print("FIM")