import socket
from urllib.parse import urlparse, urlsplit


def get_url(url):
    """通過socket 請求request"""
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'

    # 建立socket連接
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send(f'GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection:close\r\n\r\n'.encode('utf8'))

    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf8')
    # html_data = data.split('\r\n\r\n')[1]
    print(data)
    client.close()


get_url('http://www.baidu.com')



