#Várias formas de importar módulos

#Inteiro - import nome_modulo
#Vantagens : Você tem o namespace no módulo (nome do módulo)
#Desvantagens : Nomes grandes

import sys
print(sys.platform)
#sys.exit() #Sai do programa
#print(123)

#Partes - from nome_módulo import objeto1, objeto2
#Vantagens : nomes pequenos
#Desvantagens : Sem o namespace do módulo , corre o risco de sobreescrever a função com algum nome de variável
#Não colocar os mesmos nomes em possíveis variáveis

from sys import exit, platform

print("bla")
#exit()
print('oi')

#alias 1 - import nome_modulo as apelido
#Vantagens: VocÊ pode reserves nomes para seu código
#Desvantagens: Pode ficar fora do padrão da linguagem

import sys as s # Tentar optar pelas outras opções para não mudar o nome do módulo
sys = 'alguma coisa'
print(sys)
print(s.platform)


from sys import platform as pf
from  sys import exit as ex
200
# Má prática - from nome_módulo *
#Vantagens : importa tudo de um módulo
#Desvantagens : importa tudo de um módulo, corre o risco de sobreescrever com variáveis, afinal, não estou vendo os nomes.

from sys import *

print(platform)
exit()

