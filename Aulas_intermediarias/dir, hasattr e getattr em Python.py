#Dir, hasattr e getattr em Python

string = 'Reginaldo'
metodo = "upper"

print(string.upper())
print(dir(string))

#Com o DIR, consigo identificar (checar) os métodos que posso vir a utilizar.


if hasattr(string, metodo):
    print("Existe upper")
    print(getattr(string, metodo)())
    print(string)
else:
    print("Não existe o método", metodo)

#Essa aula, pode ser muito interessante em projetos futuros.


