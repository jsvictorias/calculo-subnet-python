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
    
    # Lista dos itens do exercício - TODOS como strings de máscara
    exercicios = [
        ("3.1", "255.255.192.0"),
        ("3.2", "255.255.248.0"),
        ("3.3", "255.255.255.224"),
        ("3.4", "255.255.255.128"),
        ("3.5", "255.254.0.0"),
        ("3.6", "122"),  # Agora é string "122" (provavelmente máscara incompleta)
        ("3.7", "130"),  # Agora é string "130"  
        ("3.8", "126"),  # Agora é string "126"
        ("3.9", "110"),  # Agora é string "110"
        ("3.10", "10")   # Agora é string "10"
    ]
    
    for num, valor in exercicios:
        print(f"\n🌸 {num} - {valor}")
        print("-" * 30)
        
        # Verificar se é uma máscara IPv4 completa
        if '.' in valor:
            # É máscara decimal completa (ex: 255.255.192.0)
            info = mascara_para_info(valor)
            print(f"Máscara: {valor}")
            print(f"Notação CIDR: /{info['cidr']}")
            print(f"Bits para host: {info['bits_host']}")
            print(f"Total de endereços: {info['total_enderecos']}")
            print(f"Hosts válidos: {info['hosts_validos']}")
            
        else:
            # Pode ser CIDR ou máscara incompleta - vamos interpretar como número
            try:
                numero = int(valor)
                
                # Se o número for pequeno (<= 32), interpretar como CIDR
                if numero <= 32:
                    info = cidr_para_info(numero)
                    print(f"Notação CIDR: /{numero}")
                    print(f"Máscara correspondente: {calculo_mascara(numero)}")
                    print(f"Bits para host: {info['bits_host']}")
                    print(f"Total de endereços: {info['total_enderecos']}")
                    print(f"Hosts válidos: {info['hosts_validos']}")
                
                # Se o número for grande, interpretar como número de hosts
                else:
                    cidr_str = calculo_cidr(numero)
                    cidr_num = int(cidr_str.strip('/'))
                    info = cidr_para_info(cidr_num)
                    
                    print(f"Número fornecido: {numero}")
                    print(f"Interpretado como: {numero} hosts necessários")
                    print(f"Notação CIDR necessária: {cidr_str}")
                    print(f"Máscara: {calculo_mascara(cidr_num)}")
                    print(f"Hosts suportados: {info['hosts_validos']}")
                    
            except ValueError:
                print(f"⚠️ Valor inválido: {valor}")

if __name__ == "__main__":
    ex3()