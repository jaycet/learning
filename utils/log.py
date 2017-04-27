from time import (localtime,
                  strftime,
                  )


def format_datetime():
    t= localtime()
    t = strftime('%Y-%m-%d %H:%M:%S', t)
    return t


def log(*args, **kwargs):
    t = format_datetime()
    return print(t, *args, **kwargs)

if __name__ == '__main__':
    log(1)