# EXERCÍCIO RESOLVIDO, ANTES DE VER A RESOLUÇÃO DO PROFESSOR.

# CPF de exemplo (não existe) = 168.995.350-09
#      COMO VAI FUNCIONAR O ALGORITMO
#PEGAR OS 9 PRIMEIROS DIGITOS E MULTIPLICAR CONTAGEM REGRESSIVA DE 10 ATÉ 2
#SOMAR O RESULTADO DAS MULTIPLICAÇÕES

#11 - (RESULTADO % 11) = 11 TEM QUE DAR O RESULTADO 11
#11 > 9 = 0 SE FOR MAIOR QUE 9, O RESULTADO É 0

#PARA ENCONTRAR DIGITO, CASO NÃO SEJA MAIOR QUE 9, FAZER NOVAMENTE A CONTA ANTERIOR, COMEÇANDO DO REGRESSIVO 11

#PARA VALIDAR, PEGAR OS 9 PRIMEIROS DIGITOS E + OS DOIS DIGITOS QUE FORAM GERADOS.

CPF = input("Digite um CPF:")

CPF = CPF.replace('.','')
CPF = CPF.replace('-','')
CPF_FORMATADO = CPF[:11]
CPF = CPF[:9]

regressivo = 10
soma = 0
for i in CPF:
    i = int(i)
    soma += i * regressivo
    regressivo -= 1

conta = 11 - (soma % 11) # fórmula
digito_1 = conta if conta <= 9 else 0

digito_1 = str(digito_1)
CPF = CPF + digito_1

regressivo = 11
soma2 = 0

for ii in CPF:
    ii = int(ii)
    soma2 += ii * regressivo
    regressivo -= 1

conta2 = 11 - (soma2 % 11) # fórmula
digito_2 = conta2 if conta2 <= 9 else 0
digito_2 = str(digito_2)

CPF_FINAL = CPF+digito_2

if CPF_FINAL == CPF_FORMATADO:
    print(f"O CPF: {CPF_FINAL} é Valido.")
else:
    print(f'O CPF: {CPF_FINAL} é Inválido!')




