import socket

def TCPserver(host, port):
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((host, port))
    tcp_server.listen()
    conn, addr = tcp_server.accept()

    while 1:
        data = conn.recv(1024)
        if not data:
            break
        
        msg = 'Hello, world! From ' + str(host) + ':' + str(port)
        msg_bits = msg.encode('utf_8')
        if msg_bits == data:
            print('Servidor recebeu a mensagem correta')
            conn.send(b'Sucesso')
        else: 
            print('Servidor nao recebeu a mensagem correta')
            conn.send(b'Erro')
            
    conn.close()