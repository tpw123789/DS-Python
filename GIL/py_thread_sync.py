import dis
import threading
from threading import Lock, RLock
"""
RLock: 可重入的鎖
在同一線程裡面，可連續多次acquire，但acquire的次數須和release的次數相同
"""


total = 0
lock = RLock()


def add():
    global total
    global lock
    for _ in range(1000000):
        lock.acquire()  # 獲取鎖
        lock.acquire()
        total += 1
        lock.release()  # 釋放鎖
        lock.release()


def desc():
    global total
    global lock
    for _ in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


def add1(a):
    a += 1


def desc1(a):
    a -= 1


# 字節碼
"""
1. load a
2. load 1
3. +
4. 賦值給a
"""

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)

# print(dis.dis(add1))
# print(dis.dis(desc1))

"""
1. 鎖影響性能
2. 鎖引起死鎖
死鎖情況:
互相等待，競爭資源
A(a, b)
acquire(a)
acquire(b)

B(a, b)
acquire(b)
acquire(a)
"""
