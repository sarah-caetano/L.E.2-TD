import socket
def TCPclient (host, port):
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect((host, port))

    msg = "Hello, world! From " + host + ':' + str(port)
    status = tcp_client.send(msg.encode('utf-8'))
    
    if status > 0:
        data = tcp_client.recv(1024)
        print('Saida:', data.decode('utf-8'))
    tcp_client.close()