from utils.log import log
import socket
import urllib
from routes import route_dict


class Request():
    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.query = {}
        self.body = ''

    def form(self):
        body = urllib.parse.unquote(self.body)
        args = body.split('&')
        f = {}
        for arg in args:
            k,  v = arg.split('=')
            f[k] = v
        return f


request = Request()


def route_image():
    header = b'HTTP/1.1 200 ok\r\nContent-Type: image/gif\r\n'
    with open('static/doge.gif', 'rb') as f:
        return header + b'\r\n' + f.read()


def error(code=404):
    e = {
        code: b'HTTP/1.1 404 NotFound\r\n\r\n<h1>not found<h1>'
    }
    return e.get(code, b'')


def response_for_path(path):
    r = {
        '/doge.gif': route_image
    }
    r.update(route_dict)
    response = r.get(path, error)
    return response()


def run(host='', port=3000):
    with socket.socket() as s:
        s.bind((host, port))
        while True:
            s.listen(5)
            connection, address = s.accept()
            buffer_size = 1000
            r = b''
            while True:
                recv = connection.recv(buffer_size)
                r += recv
                if len(recv) < buffer_size:
                    break
            r = r.decode('utf-8')
            log('ip and request, {} \n{}'.format(address, request))
            try:
                path = r.split()[1]
                request.method = r.split()[0]
                request.body = r.split('\r\n\r\n', 1)[1]
                response = response_for_path(path)
                connection.sendall(response)
            except Exception as e:
                log('error', e)
            connection.close()


def main():
    config = dict(
        host='',
        port=3000,
    )
    run(**config)


if __name__ == '__main__':
    main()