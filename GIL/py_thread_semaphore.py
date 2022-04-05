import threading

# Semaphore適用於控制進入數量的鎖
# 文件=> 讀/寫 寫一般只用於一個線程讀寫，讀可以允許有多個
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super(HtmlSpider, self).__init__()
        self.url = url
        self.sem = sem

    def run(self) -> None:
        time.sleep(2)
        print('got html text success')
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem: threading.Semaphore):
        super().__init__()
        self.sem = sem

    def run(self) -> None:
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider(f'https://google.com/{i}', self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(value=3)
    url_producer = UrlProducer(sem)
    url_producer.start()


