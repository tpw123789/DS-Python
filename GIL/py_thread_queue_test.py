#  通過queue方式進行線程間同步
from queue import Queue
import time
import threading
import var


def get_detail_html(queue):
    while True:
        url = queue.get()  # 若queue為空，會一直阻塞在這
        print('get detail html started')
        time.sleep(2)
        print('get detail html end')


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_html, args=(var.detail_url_list,))
