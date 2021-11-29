import threading
import random
import time
import sys

def Calculation (k):

    global sums

    n = round(length/N * (k+1))
    sum = 0
    if n > length:
        n = length
    for i in range (round(length/N * (k)), n):
        sum+= massiv[i]
    sums += sum

sums = 0
massiv = [1, 10, 3, 7, 4, 12, 19, 30, 4, 3, 5, 11, 15, 17, 18, 23, 24, 32, 16, 3, 2, 1, 0, 10, 21, 29, 17, 19, 2, 1, 0]
length = len(massiv)
for N in range (1, 30):
    sums = 0
    start = time.time()

    threads = [threading.Thread(target=Calculation(k)) for k in range(N)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    finish = time.time()
    timer = finish - start
    print (round (timer, 4))
