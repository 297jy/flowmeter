# coding=utf-8
import json
import uuid

from dwebsocket import accept_websocket

# 创建客户端列表，存储所有在线客户端
clients = {}


# 允许接受ws请求
@accept_websocket
def link_view(request):
    # 判断是不是ws请求
    if request.is_websocket():
        # 判断是否有客户端发来消息，若有则进行处理，若发来“test”表示客户端与服务器建立链接成功
        while True:
            message = request.websocket.wait()
            if not message:
                break
            else:
                # 保存客户端的ws对象，以便给客户端发送消息,每个客户端分配一个唯一标识
                user_id = json.loads(message)['user_id']
                clients[user_id] = request.websocket
