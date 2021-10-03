def swap(func):
   def wrapper(*args, **kwargs):
       arr = args[::-1]
       return func(*arr, **kwargs)
   return wrapper

def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res
print(div(2,4, show = False))
div = swap(div)
print(div(2,4, show = False))
