import math
def sumComple (a,b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return (real,imag)

def resComple (a,b):
    real = a[0] - b[0]
    imag = a[1] - b[1]
    return (real,imag)

def multiComple (a,b):
    real = (a[0]*b[0])-(a[1]*b[1])
    imag = (a[0]*b[1])+(a[1]*b[0])
    return (real, imag)

def modulComple (a):
    return math.sqrt((a[0]**2)+(a[1]**2))

def faseComple (a):
    result = math.atan2(a[1],a[0])
    if result < 0:
        fase = 2*math.pi - (-1)*result
        return fase
    else:
        return result


def convertpolarComple (a):
    real = modulComple(a)
    imag = faseComple(a)
    return (real,imag)

def convertnormalComple (a):
    r = a[0]
    an = a[1]
    real = r * math.cos(an)
    imag = r * math.sin(an)
    return (real, imag)

def conjugado(a):
    real = a[0]
    imag = a[1]*(-1)
    return (real, imag)

def diviComple (a,b):
    result = multiComple(a,conjugado(b))
    real = result[0] / (b[0]**2 + b[1]**2)
    imag = result[1] / (b[0]**2 + b[1]**2)
    return (real, imag)


