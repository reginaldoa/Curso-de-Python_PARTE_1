#Entendendo os seus próprios módulos python
#O primeiro módulo executado chamase __main__
#Você pode importar outro módulo inteiro ou parte do módulo
#O python conhece a pasta onde o __main__ está e  e as pastar abaixo dele
#Ele não reconhece pastas e módulos acima do __main__ por padrão
#O python cohhece todos os módulos e pacotes presentes nos caminhos de sys.path

try:
    import sys
    sys.path.append('/home') # Dá para pegar um módulo, colocando um caminho também.
except ModuleNotFoundError:
    ...
import testesmod



print("Este módulo se chama", __name__)
print(*sys.path, sep ='\n')
