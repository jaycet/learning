def template(name):
    path = 'template/' + name
    with open(path, 'rb') as f:
        return f.read()


def route_index():
    header = b'HTTP/1.1 200 ok\r\nContent-Type: text/html\r\n'
    body = template('index.html')
    r = header + b'\r\n' + body
    return r


route_dict = {
    '/': route_index,
}
