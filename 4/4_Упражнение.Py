import time
def decorator(pat):
    def decoratorr(func):
        def new_func(*args, **kwargs):

            file = open(pat, 'w')
            t1 = time.time()
            file.write(str(t1)+"\n")
            file.write(str(*args)+"\n")
            file.write(str(**kwargs)+"\n")
            a = func(*args, **kwargs)
            if a != None:
                print(a)
            else:
                print('-')
            t2 = time.time()
            file.write(str(t2)+"\n")
            file.write(str((t2 - t1))+"\n")
            file.close()

            return a

        return new_func

    return decoratorr
pat = 'C:\\Users\\User\\Desktop\\4_Упражнение.txt'
@decorator(pat)
def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)
fibb(7)
