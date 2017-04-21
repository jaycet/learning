import socket


host = ''
port = 2000
s = socket.socket()
s.bind((host, port))
while True:
    s.listen(5)
    connection, address = s.accept()
    request = connection.recv(1024)
    response = b'HTTP/1.1 200 very ok\r\n\r\n<h1>hello world<h1>'
    connection.sendall(response)
    connection.close()