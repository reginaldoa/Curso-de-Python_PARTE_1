#Raise - lançando exceções (erros)

def nao_aceito_Zero(d):
    if d == 0:
        raise ZeroDivisionError("Você está tentando dividir por zero")
    return True


def deve_Ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float.'
            f'{tipo_n} enviado'
        )
       


def divide(n , d):
    nao_aceito_Zero(d)
    deve_Ser_int_ou_float(n)
    deve_Ser_int_ou_float(d)
    return n / d

    

print(divide(8,'0'))