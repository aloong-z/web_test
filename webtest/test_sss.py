import socket
import time

sk = socket.socket()
sk.bind(("127.0.0.1", 8093))  # 绑定IP和端口
sk.listen()  # 监听


# 将返回不同的内容部分封装成函数
def house(url):
    print(url)
    with open("house.html", "r", encoding="utf8") as f:
        s = f.read()
        # now = str(time.time())
        s = s.replace("@@oo@@", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 在网页中定义好特殊符号，用动态的数据去替换提前定义好的特殊符号
    return bytes(s, encoding="utf8")


def home(url):
    print(url)
    with open("home.html", "r", encoding="utf8") as f:
        s = f.read()
    return bytes(s, encoding="utf8")


# 定义一个url和实际要执行的函数的对应关系
list1 = [
    ("/home/", home),
    ("/house/", house),
]

while 1:
    # 等待连接
    conn, add = sk.accept()
    data = conn.recv(8096)  # 接收客户端发来的消息
    # 从data中取到路径
    data = str(data, encoding="utf8")  # 把收到的字节类型的数据转换成字符串
    # 按\r\n分割
    data1 = data.split("\r\n")[0]
    urls = data1.split()[1]  # url是我们从浏览器发过来的消息中分离出的访问路径
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')  # 因为要遵循HTTP协议，所以回复的消息也要加状态行
    # 根据不同的路径返回不同内容
    func = None  # 定义一个保存将要执行的函数名的变量
    for i in list1:
        if i[0] == urls:
            func = i[1]
            break
    if func:
        response = func(urls)
    else:
        response = b"404 not found!"

    # 返回具体的响应消息
    conn.send(response)
    conn.close()
