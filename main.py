from utils.calculo_cidr.main import calculo_cidr
from utils.calculo_mascara.main import calculo_mascara
from utils.calculo_subnet.main import calculo_subnet

cenario = {
    'lapa': 1800,
    'cambuci': 1500,
    'pinheiros': 1900,
    'osasco': 1400,
    'jandira': 1200,
    'carapicuiba': 1750
}

ip_fornecido = '172.19.0.0'

def main():

    """
        Função principal que baseada no cenário e no IP fornecido calculo a Subnet,
        Notação CIDR, Máscara de Rede e Máscara Curinga.
    """

    print("=" * 60)
    print("          🎀 CÁLCULO DE SUB-REDES PARA CENÁRIO 🎀")
    print("=" * 60)
    print(f"IP base: {ip_fornecido}")
    print("=" * 60)
    
    for bairro, hosts_necessarios in cenario.items():
        print(f"\n 🌸 {bairro.upper()} - {hosts_necessarios} hosts necessários")
        print("-" * 40)
        
        # Calcular CIDR
        cidr = calculo_cidr(hosts_necessarios)
        print(f"Notação CIDR: {cidr}")
        
        # Extrair número do CIDR para cálculos
        cidr_numero = int(cidr.strip('/'))
        
        # Calcular máscara de rede
        mascara_rede = calculo_mascara(cidr_numero, coringa=False)
        print(f"Máscara de Rede: {mascara_rede}")
        
        # Calcular máscara curinga
        mascara_curinga = calculo_mascara(cidr_numero, coringa=True)
        print(f"Máscara Curinga: {mascara_curinga}")
        
        # Calcular informações da sub-rede
        info_subnet = calculo_subnet(ip_fornecido, cidr_numero, mascara_rede)
        print(f"\nInformações da Sub-rede:")
        print(info_subnet)

if __name__ == "__main__":
    main()