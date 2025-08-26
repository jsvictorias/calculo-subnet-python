from utils.calculo_mascara.main import calculo_mascara

def ex5():
    """
    Converte máscaras de sub-rede e notação CIDR para máscara curinga
    """
    print("=" * 50)
    print("🎀 Exercício 5 - Conversão para Máscara Curinga 🎀")
    print("=" * 50)
    
    # Lista dos itens do exercício
    itens = [
        ("5.1", "255.255.240.0"),
        ("5.2", "255.255.224.0"),
        ("5.3", "/22"),
        ("5.4", "/28"),  
        ("5.5", "255.192.0.0"),
        ("5.6", "/10"),
        ("5.7", "255.255.128.0"),
        ("5.8", "/30"),
        ("5.9", "255.255.254.0"),
        ("5.10", "255.255.255.252")
    ]
    
    for num, valor in itens:
        print(f"\n🌸 {num} - {valor}")
        print("-" * 30)
        
        if isinstance(valor, str) and valor.startswith('/'):
            cidr = int(valor[1:])
            mascara = calculo_mascara(cidr, coringa=False)
            mascara_curinga = calculo_mascara(cidr, coringa=True)
            print(f"Notação CIDR: {valor}")
            print(f"Máscara de rede: {mascara}")
            print(f"Máscara curinga: {mascara_curinga}")
            
        else:
            cidr = mascara_para_cidr(valor)
            mascara_curinga = calculo_mascara(cidr, coringa=True)
            print(f"Máscara de rede: {valor}")
            print(f"Notação CIDR: /{cidr}")
            print(f"Máscara curinga: {mascara_curinga}")

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
            bits = bin(valor)[2:].zfill(8)
            cidr += bits.count('1')
            break
    
    return cidr

if __name__ == "__main__":
    ex5()