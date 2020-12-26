import socket
from threading import Thread

sk = socket.socket()
sk.bind(('127.0.0.1', 8091))
sk.listen()


def test_html(conn):
    conn.send(b'HTTP/1.1 200 ok\r\ncontent-type:text/html\r\ncharset:utf-8\r\n\r\n')
    with open('test.html', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()


def test_jpg(conn):
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    with open('lover.jpg', 'rb') as f:
        pic_data = f.read()
    conn.send(pic_data)
    conn.close()


def test_css(conn):
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    with open('test.css', 'rb') as f:
        css_data = f.read()
    conn.send(css_data)
    conn.close()


def test_ico(conn):
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    with open('logo.ico', 'rb') as f:
        ico_data = f.read()
    conn.send(ico_data)
    conn.close()


def test_js(conn):
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    with open('test.js', 'rb') as f:
        js_data = f.read()
    conn.send(js_data)
    conn.close()


# 定义一个路径和执行函数的对应关系，不再写一堆的if判断了
l1 = [
    ('/', test_html),
    ('/lover.jpg', test_jpg),
    ('/test.css', test_css),
    ('/logo.ico', test_ico),
    ('/test.js', test_js),
]


# 遍历路径和函数的对应关系列表，并开多线程高效的去执行路径对应的函数
def fun(path, conn):
    for i in l1:
        if i[0] == path:
            t = Thread(target=i[1], args=(conn,))
            t.start()


while 1:
    con, url = sk.accept()
    # 看完这里面的代码之后，你就可以思考一个问题了，很多人要同时访问你的网站，你在请求这里是不是可以开起并发编程的思想了，多进程+多线程+协程，妥妥的支持高并发，再配合服务器集群，这个网页就支持大量的高并发了，有没有很激动，哈哈，但是咱们写的太low了，而且功能很差，容错能力也很差，当然了，如果你有能力，你现在完全可以自己写web框架了，写一个nb的，如果现在没有这个能力，那么我们就来好好学学别人写好的框架把，首先第一个就是咱们的django框架了，其实就是将这些功能封装起来，并且容错能力强，抗压能力强，总之一个字：吊。
    from_b_msg = con.recv(1024)
    str_msg = from_b_msg.decode('utf-8')
    pat = str_msg.split('\r\n')[0].split(' ')[1]
    print('path>>>', pat)
    # 注意：因为开启的线程很快，可能导致你的文件还没有发送过去，其他文件的请求已经来了，导致你文件信息没有被浏览器正确的认识，所以需要将发送请求行和请求头的部分写道前面的每一个函数里面去，并且防止出现浏览器可能不能识别你的html文件的情况，需要在发送html文件的那个函数里面的发送请求行和请求头的部分加上两个请求头content-type:text/html\r\ncharset:utf-8\r\n

    print(from_b_msg)
    fun(pat, con)
