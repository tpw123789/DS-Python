# 對IO操作來說，多進程和多線程性能差別不大
# 通過Thread類實例化
import time
import threading


def get_detail_html(url):
    print('get detail html started')
    time.sleep(2)
    print('get detail html end')


def get_detail_url(url):
    print('get detail url started')
    time.sleep(4)
    print('get detail url end')


# 通過繼承Thread來實現多線程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super(GetDetailHtml, self).__init__(name=name)

    def run(self) -> None:
        print('get detail html started')
        time.sleep(2)
        print('get detail html end')


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super(GetDetailUrl, self).__init__(name=name)

    def run(self):
        print('get detail url started')
        time.sleep(4)
        print('get detail url end')


if __name__ == '__main__':
    # thread1 = threading.Thread(target=get_detail_html, args=('',))
    # thread2 = threading.Thread(target=get_detail_url, args=('',))
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)
    thread1 = GetDetailHtml(name='get_detail_html')
    thread2 = GetDetailUrl(name='get_detail_url')
    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(f'last time {time.time() - start_time}')

