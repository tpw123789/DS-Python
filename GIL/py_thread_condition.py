import threading
from threading import Condition
# 條件變量，用於複雜的線程間同步


# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name='小愛')
#         self.lock = lock
#
#     def run(self) -> None:
#         self.lock.acquire()
#         print(f'{self.name}: 在')
#         self.lock.release()
#
#         self.lock.acquire()
#         print(f'{self.name}: 好啊')
#         self.lock.release()
#
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name='天貓')
#         self.lock = lock
#
#     def run(self) -> None:
#         self.lock.acquire()
#         print(f'{self.name}: 小愛')
#         self.lock.release()
#
#         self.lock.acquire()
#         print(f'{self.name}: 聊天')
#         self.lock.release()


class XiaoAi(threading.Thread):
    def __init__(self, condition: Condition):
        super().__init__(name='小愛')
        self.condition = condition

    def run(self) -> None:
        with self.condition:
            self.condition.wait()
            print(f'{self.name}: 在')
            self.condition.notify()

            self.condition.wait()
            print(f'{self.name}: 好啊')
            self.condition.notify()


class TianMao(threading.Thread):
    def __init__(self, condition: Condition):
        super().__init__(name='天貓')
        # self.lock = lock
        self.condition = condition

    def run(self) -> None:
        with self.condition:
            print(f'{self.name}: 小愛')
            self.condition.notify()
            self.condition.wait()

            print(f'{self.name}: 來聊天')
            self.condition.notify()
            self.condition.wait()


if __name__ == '__main__':
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    # 啟動順序很重要
    # notify和wait方法須在condition.acquire()之後
    # condition有兩層鎖，一把底層鎖會在調用wait方法時釋放，上面的鎖會在每次調用wait方法時分配一把並放到condition的等待dequeue中
    # 等到notify方法喚醒
    xiaoai.start()
    tianmao.start()
