from random import randint

def decorator(function):

    def new_even(*args):
        if args[2] < 0:
            print('Нет')
        elif args[2] > 10:
            print('Очень много')
        else:
            print('Чуть-чуть есть')
    return new_even
N = randint(1, 10)
a = [randint(1, 30) for i in range(N)]
print(a)
count = 0
def even(a, N, count):
    for i in range(N):
        if a[i] % 2 == 0:
            count += 1
    return count
print(even(a, N, count))
even = decorator(chet)
even(a, N, count)
