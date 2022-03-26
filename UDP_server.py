import socket
def UDPserver(host, port):
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind((host, port))
    while 1:
        data, address = udp_server.recvfrom(1024)
        if not data:
            break
        msg = 'Hello, world! From ' + str(host) + ':' + str(port)
        msg_bits = msg.encode('utf_8')
        if msg_bits == data:
            print('Servidor recebeu a mensagem correta')
            udp_server.sendto(b'Sucesso', address)
        else: 
            print('Servidor nao recebeu a mensagem correta')
            udp_server.sendto(b'Erro', address)
    udp_server.close()