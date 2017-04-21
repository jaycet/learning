import socket


s = socket.socket()

# https连接如下：
# import ssl
# s = ssl.wrap_socket(socket.socket())
host = 'www.harmontronics.com'
port = 80
s.connect((host, port))
ip, port = s.getsockname()
print('本机的ip：{}，port：{}'.format(ip, port))
http_request = 'GET / HTTP/1.1\r\nhost: {}:{}\r\nConnection: close\r\n\r\n'.format(host, port)
request = http_request.encode('utf-8')
s.send(request)
response = s.recv(1023)
print(response.decode('utf-8'))
