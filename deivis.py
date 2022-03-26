import socket
def UDPserver(host, port):
    global udpd 
    udpd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpd.bind((host, port))
    while 1:
        data, address = udpd.recvfrom(1024)
        if not data:
            break
        senha = data.decode('utf-8')
        maiuscula = 0
        minuscula = 0
        tam_err = 0
        numero = 0
        nao_char = 0
        if (len(senha) < 6 or len(senha) > 32):
            tam_err +=1
        else:
            for char in senha:
                if (char >= 'A' and char <= 'Z'):
                    maiuscula +=1
                elif (char >= 'a' and char <= 'z'):
                    minuscula +=1
                elif (char >= '0' and char <= '9'):
                    numero +=1
                else:
                    nao_char +=1
                    break
        if(tam_err > 0 or maiuscula == 0 or minuscula == 0 or numero == 0 or nao_char > 0):
            invalida = "Senha inválida!"
            invalida_bits = invalida.encode('utf-8')
            udpd.sendto(invalida_bits, address)
        else: 
            valida = "Senha valida."
            valida_bits = valida.encode('utf-8')
            udpd.sendto(valida_bits, address)
    udpd.close()