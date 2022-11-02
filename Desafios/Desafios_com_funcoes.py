#Todos os exercícios, foram feitos antes da ver a resolução do professor.

# 1 -Criar função que exibe uma saudação com os parâmetros saudação e nome

# 2 - Crie função que recebe 3 números como parâmetro e exiba a soma entre eles.

# 3 - Crie função que recebe 2 números. O primeiro é um valor e o segundo um percentual.
# Retorne o valor do primeiro numero somado do aumento do percentual do mesmo


# 4 - Fizz buzz - se o parametro da função for divisivel por 2, retorne fizz,
# se for divisivel por 5, retorn buzz. Se o parametro da função for divisivel por 5 e por 3, retorne FizzBuzz
#Caso contrario, retorne  o número enviado.

#Exercicio 1
def saudacoes(saudacao, nome):
    return f"{saudacao} {nome}, seja bem vindo"

bem_vindo = saudacoes("oi", "Reginaldo")
print(bem_vindo)



#Exercício 2
def somar(num1, num2, num3):
    return num1 + num2 + num3

conta = somar(5,5,5)
print(conta)

#Exercício 3
def percentual(numero, porcentagem):
    return numero/100 * porcentagem + numero

conta_porcento = percentual(89,30)
print(conta_porcento)


#Exercício 4

def FB(numero):
    return numero

resposta = FB(20)

if resposta %2 == 0 and resposta %5 ==0:
    print("FizzBuzz")
elif resposta % 2 == 0:
    print("Fizz")
elif resposta % 5 == 0:
    print("Buzz")
else:
    print(resposta)


