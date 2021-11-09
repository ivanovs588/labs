import numpy as np


class PrintVariance(Exception):
    pass


class PrintMean(Exception):
    pass


class PrintCount(Exception):
    pass


def server_coroutine():
    print("Starting coroutine")
    data = []
    try:
        while True:
            try:
                to_add = yield
                data.append(to_add)
            except PrintVariance:
                yield np.var(data)
            except PrintMean:
                yield np.mean(data)
            except PrintCount:
                yield len(data)
    finally:
        print("Stop coroutine")


coroutine = server_coroutine()
next(coroutine)
i = int(input())
while i != 0:
    coroutine.send(i)
    if i % 2 == 0:
        print("Current variance:", coroutine.throw(PrintVariance))
        next(coroutine)
    if i % 3 == 0:
        print("Current mean:", coroutine.throw(PrintMean))
        next(coroutine)
    if i % 5 == 0:
        print("Current count:", coroutine.throw(PrintCount))
        next(coroutine)
    i = int(input())

coroutine.close()
