import ipaddress

def calculo_subnet(ip: str, cidr, mascara):
    """
    """

    rede = ipaddress.ip_network(f'{ip}/{cidr}', strict=False)


    broadcast = str(rede.broadcast_address)

    hosts = list(rede.hosts())
    primeiro_host = str(hosts[0])
    ultimo_host = str(hosts[-1])
    return "\n".join([
        f"{'Mascara':<15} => {mascara}",
        f"{'Rede':<15} => {rede}",
        f"{'Broadcast':<15} => {broadcast}",
        f"{'Primeiro_host':<15} => {primeiro_host}",
        f"{'Ultimo_host':<15} => {ultimo_host}",
        f"{'Total_hosts':<15} => {len(hosts)}"
    ])

