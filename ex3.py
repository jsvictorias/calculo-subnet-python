from utils.calculo_cidr.main import calculo_cidr
from utils.calculo_mascara.main import calculo_mascara


def mascara_para_cidr(mascara):
    """
    Converte máscara decimal para notação CIDR
    """
    octetos = mascara.split('.')
    cidr = 0
    
    for octeto in octetos:
        valor = int(octeto)
        if valor == 255:
            cidr += 8
        elif valor == 0:
            break
        else:
            # Contar bits '1' no octeto
            bits = bin(valor)[2:].zfill(8)
            cidr += bits.count('1')
            break
    
    return cidr

def cidr_para_info(cidr):
    """
    Calcula informações a partir do CIDR
    """
    bits_host = 32 - cidr
    total_enderecos = 2 ** bits_host
    hosts_validos = max(0, total_enderecos - 2) 
    
    return {
        'cidr': cidr,
        'bits_host': bits_host,
        'total_enderecos': total_enderecos,
        'hosts_validos': hosts_validos,
    }

def mascara_para_info(mascara):
    """
    Calcula informações a partir da máscara
    """
    cidr = mascara_para_cidr(mascara)
    info = cidr_para_info(cidr)
    info['mascara'] = mascara
    return info

def ex3():
    """
    Identifica a variação e hosts válidos das máscaras de sub-rede e notação CIDR
    """
    print("=" * 40)
    print("           🎀 Exercício 3 🎀")
    print("=" * 40)
    
    # Lista dos itens do exercício
    exercicios = [
        ("3.1", "255.255.192.0"),
        ("3.2", "255.255.248.0"),
        ("3.3", "255.255.255.224"),
        ("3.4", "255.255.255.128"),
        ("3.5", "255.254.0.0"),
        ("3.6", 26),  
        ("3.7", 25),    
        ("3.8", 25),  
        ("3.9", 25),  
        ("3.10", 10)  
    ]
    
    for num, valor in exercicios:
        print(f"\n🌸 {num} - {valor}")
        print("-" * 30)
        
        if isinstance(valor, int):
            # É notação CIDR (número)
            info = cidr_para_info(valor)
            print(f"Notação CIDR: /{valor}")
            print(f"Máscara correspondente: {calculo_mascara(valor)}")
        else:
            # É máscara decimal (string)
            info = mascara_para_info(valor)
            print(f"Máscara: {valor}")
            print(f"Notação CIDR: /{info['cidr']}")
        
        print(f"Bits para host: {info['bits_host']}")
        print(f"Total de endereços: {info['total_enderecos']}")
        print(f"Hosts válidos: {info['hosts_validos']}")

def ex3_alternativo():
    """
    Interpreta 3.6-3.9 como número de hosts necessários
    """
    print("\n" + "=" * 60)
    print("🎀 Exercício 3 - Interpretação Alternativa (como hosts) 🎀")
    print("=" * 60)
    
    hosts_items = [
        ("3.6", 122),
        ("3.7", 130), 
        ("3.8", 126),
        ("3.9", 110)
    ]
    
    for num, hosts in hosts_items:
        print(f"\n🌸 {num} - {hosts} hosts necessários")
        print("-" * 40)
        
        # Usar sua função calculo_cidr existente
        cidr_str = calculo_cidr(hosts)
        cidr_num = int(cidr_str.strip('/'))
        
        print(f"Hosts necessários: {hosts}")
        print(f"Notação CIDR necessária: {cidr_str}")
        print(f"Máscara: {calculo_mascara(cidr_num)}")
        
        info = cidr_para_info(cidr_num)
        print(f"Hosts suportados: {info['hosts_validos']}")

if __name__ == "__main__":
    ex3()
    ex3_alternativo()