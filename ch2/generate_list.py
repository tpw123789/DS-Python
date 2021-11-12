import timeit
from threading import Timer


def test1():
    pool = []
    for i in range(1000):
        pool += [i]
    
    
def test2():
    pool = []
    for i in range(1000):
        pool.append(i)


def test3():
    pool = [i for i in range(1000)]


def test4():
    pool = list(range(1000))


t1 = timeit.Timer("test1()", "from __main__ import test1")
t2 = timeit.Timer("test2()", "from __main__ import test2")
t3 = timeit.Timer("test3()", "from __main__ import test3")
t4 = timeit.Timer("test4()", "from __main__ import test4")
print('concat', t1.timeit(number=1000), 'milliseconds')
print('append', t2.timeit(number=1000), 'milliseconds')
print('comprehension', t3.timeit(number=1000), 'milliseconds')
print('list range', t4.timeit(number=1000), 'milliseconds')

