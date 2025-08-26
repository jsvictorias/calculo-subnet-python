import math

def calculo_cidr(host_inicial):
    """
        Converte um host para achar o CIDR
    """
    # Acha a potência de 2 mais próxima que é a quantidade de bits para host.

    host_valido = host_inicial + 2 # por que inclui rede e broadcast

    if host_valido <= 0:
       return 1, 0
    
    expoente = math.ceil(math.log2(host_valido))

    cidr = 32 - expoente
    return f'/{cidr}'

