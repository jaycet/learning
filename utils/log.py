from time import (localtime,
                  strftime,
                  )


def format_datetime():
    t= localtime()
    t = strftime('%Y-%m-%d %H:%M:%S', t)
    return t


def log(*args, **kwargs):
    t = format_datetime()
    with open('log.txt', 'a+') as f:
        print(t, *args, **kwargs, file=f)

if __name__ == '__main__':
    log('12345')