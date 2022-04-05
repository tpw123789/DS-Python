import threading
import time

detail_url_list = []


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super(GetDetailHtml, self).__init__(name=name)

    def run(self) -> None:
        global detail_url_list
        url = detail_url_list.pop()

        print('get detail html started')
        time.sleep(2)
        print('get detail html end')


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super(GetDetailUrl, self).__init__(name=name)

    def run(self):
        global detail_url_list
        print('get detail url started')
        time.sleep(4)
        for i in range(20):
            detail_url_list.append('example url')
        print('get detail url end')


# 線程通信方式
# 共享變數
