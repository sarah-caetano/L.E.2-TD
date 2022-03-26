import socket
def TCPserver (host,port):
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((host, port))
    tcp_server.listen()
    conn, addr = tcp_server.accept()
    while 1:
        data = conn.recv(1024)
        if not data: 
            break
        msg = data.decode('utf8') 
        # logica
        result = ""    
        cont = 0    
        for char in msg:
            if not result:
                result += char
                cont += 1
            elif(result[-1] == char):
                cont+=1
            else:
                result += str(cont)
                result += char
                cont = 1
        result += str(cont)
        resultado = result.encode('utf-8')
        conn.send(resultado)
    conn.close()
