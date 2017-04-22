import socket
import ssl
from parseurl import parseurl


def socket_by_protocol(protocol):
    if protocol == 'http':
        return socket.socket()
    else:
        return ssl.wrap_socket(socket.socket())


def get(url):
    protocol, host, port, path = parseurl(url)
    s = socket_by_protocol(protocol)
    s.connect((host, port))
#    ip, port = s.getsockname()
#    print('本机的ip：{}，port：{}'.format(ip, port))
    http_request = 'GET {} HTTP/1.1\r\nhost: {}\r\nConnection: close\r\n\r\n'.format(path, host)
    request = http_request.encode('utf-8')
    s.send(request)
    buffer_size = 1000
    r = b''
    while True:
        response = s.recv(buffer_size)
        r += response
        if len(response) < 1000:
            break
    r = r.decode('utf-8')
    status_code, headers, body = parse_response(r)
    if status_code == 301:
        url = headers['Location']
        return get(url)
    return status_code, headers, body


def parse_response(r):
    header, body = r.split('\r\n\r\n', 1)
    h = header.split('\r\n')
    status_code = h[0].split()[1]
    status_code = int(status_code)
    headers = {}
    for line in h[1:]:
        k, v = line.split(': ')
        headers[k] = v
    return status_code, headers, body


if __name__ == '__main__':
    u = 'movie.douban.com'
    for i in get(u):
        print(i)
