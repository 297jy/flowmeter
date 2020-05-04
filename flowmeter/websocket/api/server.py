# encoding=utf-8

import threading
from flowmeter.websocket.core import server as server_core


def server_socket():
    notice_thread = threading.Thread(target=server_core.notice_user)
    notice_thread.start()
    server_thread = threading.Thread(target=server_core.run)
    server_thread.start()


if __name__ == "__main__":
    server_socket()