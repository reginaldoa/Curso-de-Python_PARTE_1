from sys import path

#Importando de várias formas
import aula99_package 
from aula99_package.modulo import soma
from aula99_package.modulo import soma
from aula99_package import modulo
from aula99_package.modulo import * # * significa ALL (TUDO)

#print(path, sep = '\n')

#print de acordo com as formas de importar
print(aula99_package.modulo.soma(1,2))
print(soma(1,2))
print(modulo.soma(1,2))
print(soma(1,2))
print(variavel)
print(teste)


from aula99_package.modulo import soma, fala_oi

print(__name__)

