import socket
def TCPclient(host, port):
    #instanciando o socket

    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #AF_INET = cte que informa o tipo de endereçamento utilizado (end de rede: host+porta)
    #SOCK_STREAM = tipo de dado a ser trocado (trem de bits - streaming)
    #estabelecendo uma conexão com um serviço TCP externo

    tcp_client.connect((host, port))
    # host = o IP/ nome do domínio de destino
    # port = porta numérica (int) do serviço de destino

    status = tcp_client.send(b'Hello, world') # b = convertendo a string para binário

    if status > 0:
        data = tcp_client.recv(1024)
        print('Received', repr(data)) # repr = representação
    tcp_client.close()