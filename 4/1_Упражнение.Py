import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n')
    parser.add_argument('--name', nargs='?')
    return parser

def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.n:
        print(fibb(int(namespace.n)))
    if namespace.name:
        print(fibb(int(namespace.name)))
