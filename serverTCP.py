import socket
def TCPserver(host, port):
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((host, port)) #alocação da porta pq um serviço vai começar a operar ali
    tcp_server.listen()
    conn, addr = tcp_server.accept()
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode('utf8'))
        # serviço de eco: encaminhar de volta os bits
        conn.sendall(data)

    conn.close()
