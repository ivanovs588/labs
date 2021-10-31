def zipp(*iterables):
    tmp = []
    for i in iterables:
        tmp.append(iter(i))
    while True:
        res = []
        try:
            for i in tmp:
                res.append(next(i))
            yield tuple(res)
        except StopIteration:
            break
def mapp(function, iterable):

    it = iter(iterable)
    while True:
        try:
            print(function(next(it)))
        except StopIteration:
            break
def enumerat(iterable):
    i = 0
    for j in iterable:
        yield (i,j)
        i += 1
