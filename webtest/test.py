import socket
from threading import Thread

sk = socket.socket()
sk.bind(('127.0.0.1', 8090))
sk.listen()


def test_html(conn):
    with open('test.html', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()


def test_jpg(conn):
    with open('xiaoxiao.jpg', 'rb') as f:
        pic_data = f.read()
    conn.send(pic_data)
    conn.close()


def test_css(conn):
    with open('test.css', 'rb') as f:
        ico_data = f.read()
    conn.send(ico_data)
    conn.close()


def test_ico(conn):
    with open('logo.ico', 'rb') as f:
        ico_data = f.read()
    conn.send(ico_data)
    conn.close()


def test_js(conn):
    with open('test.js', 'rb') as f:
        js_data = f.read()
    conn.send(js_data)
    conn.close()


while 1:
    con, url = sk.accept()
    from_b_msg = con.recv(1024)
    str_msg = from_b_msg.decode('utf-8')
    path = str_msg.split('\r\n')[0].split(' ')[1]
    print('path>>>', path)
    con.send(b'HTTP/1.1 200 ok \r\n\r\n')
    print(from_b_msg)
    if path == '/':
        # test_html(con)
        t = Thread(target=test_html, args=(con,))
        t.start()
    elif path == '/xiaoxiao.jpg':
        # test_jpg(con)
        t = Thread(target=test_jpg, args=(con,))
        t.start()
    elif path == '/test.css':
        # test_css(con)
        t = Thread(target=test_css, args=(con,))
        t.start()
    elif path == '/logo.ico':
        # test_ico(con)
        t = Thread(target=test_ico, args=(con,))
        t.start()
    elif path == '/test.js':
        # test_js(con)
        t = Thread(target=test_js, args=(con,))
        t.start()
