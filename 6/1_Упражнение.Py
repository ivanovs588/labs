import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):     
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(self.real * no.real, self.imaginary * no.imaginary)

    def __truediv__(self, no):
        return Complex(self.real / no.real, self.imaginary / no.imaginary)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)
    
    def __abs__(self):
        return math.sqrt(self.real * self.real + self.imaginary * self.imaginary)

    def __str__(self):
        res = ''
        if self.real != 0:
            res += str(self.real)
        if self.imaginary > 0:
            if res == '':
                res += ' {}i'.format(self.imaginary)
            else:
                res += ' + {}i'.format(self.imaginary)
        elif self.imaginary < 0:
            if res == '':
                res += ' {}i'.format(self.imaginary)
            else:
                res += ' - {}i'.format(-self.imaginary)
        else:
            pass
        return(res)


if __name__ == '__main__':
    x = Complex(2,1)
    y = Complex(5,6)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
