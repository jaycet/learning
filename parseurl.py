def parseurl(url):
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1]
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        u =url
    i = u.find('/')
    if i == -1:
        host = u
        path = '/'
    else:
        host = u[:i]
        path = u[i:]
    port_dict = dict(
        http=80,
        https=443,
    )
    port = port_dict.get(protocol)
    if ':' in host:
        h = host.split(':')
        host = h[0]
        port = int(h[1])
    return protocol, host, port, path


if __name__ == '__main__':
    u = 'https://www.baidu.com:3000/index.html'
    print(parseurl(u))