variavel = "valor"   #Está no escopo global
#a variavel global está sempre disponível dentro das funções, caso seja necessário.

def func():
    #global variavel - (para transformar a variavel global, mesmo dentro da função, porém, não é aconselhavel)
    variavel = "Outro valor" #Editando o valor da variavel na função
    print(variavel)

func()
print("##########################")
print(variavel) #Como a variavel foi editada dentro da função, ela não é editada no escopo global, apenas na função.
