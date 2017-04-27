from utils.log import log
import socket


def route_index():
    header = b'HTTP/1.1 200 ok\r\nContent-Type: text/html\r\n'
    body = b'<h1>hello world</h1><img src="/doge.gif"/>'
    r = header + b'\r\n' + body
    return r


def route_image():
    header = b'HTTP/1.1 200 ok\r\nContent-Type: image/gif\r\n'
    with open('doge.gif', 'rb') as f:
        return header + b'\r\n' + f.read()


def error(code=404):
    e = {
        code: b'HTTP/1.1 404 NotFound\r\n\r\n<h1>not found<h1>'
    }
    return e.get(code, b'')


def response_for_path(path):
    r = {
        '/': route_index,
        '/doge.gif': route_image,
    }
    response = r.get(path, error)
    return response()


def run(host='', port=3000):
    with socket.socket() as s:
        s.bind((host, port))
        while True:
            s.listen(5)
            connection, address = s.accept()
            request = connection.recv(1024)
            request = request.decode('utf-8')
            log('ip and request, {} \n{}'.format(address, request))
            try:
                path = request.split()[1]
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