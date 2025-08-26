def calculo_mascara(cidr: int, coringa=False):
    """
        Cálcula a Máscara, o parametro coringa diz se quer a máscara coringa ou não
    """

    if cidr < 0 or cidr > 32:
        print("⚠️ CIDR deve estar entre 0 e 32")
    else: 
        mascara = []
        bits_restantes = cidr

        for i in range(1, 5):
            if bits_restantes >= 8:
                mascara.append(255)
                bits_restantes -= 8
            else:
                valor = (256 - (1 << (8 - bits_restantes))) if bits_restantes > 0 else 0
                mascara.append(valor)
                bits_restantes = 0

        if coringa:
            mascara = [255 - x for x in mascara]

    return ".".join(map(str, mascara))
