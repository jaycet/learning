import socket


host = ''
port = 2000
s = socket.socket()
s.bind((host, port))
while True:
    s.listen(5)
    connection, address = s.accept()
    buffer_size = 1000
    r = b''
    while True:
        request = connection.recv(buffer_size)
        if len(request) < buffer_size:
            break
    response = b'HTTP/1.1 200 very ok\r\n\r\n<h1>hello world<h1>'
    connection.sendall(response)
    connection.close()