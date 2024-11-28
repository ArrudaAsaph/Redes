def binn(ip):
    a = ""
    for i in (ip): 
        a += bin(int(i))[2:].zfill(8)
    return  a

def same_network(ip1, ip2, mask):
    if not(0 <= mask <= 32):
        raise ValueError("Mascara inválida!")

    bin_ip1 = binn(ip1.split('.'))[:mask]
    bin_ip2 = binn(ip2.split('.'))[:mask]

    return bin_ip1 == bin_ip2

ip1 = input("Digite o primeiro ip: ")
ip2 = input("Digite o segundo ip: ")
mask = int(input("Digite a mascara de rede (em decimal): "))
print(same_network(ip1,ip2,mask))
    


