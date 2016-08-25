__author__ = 'Alex'
a = 11

def bi(i):
    #binary
    z = ""
    while i > 0:
        y = str(i % 2)
        z = y + z
        i = int(i / 2)
    return z

def octal(i):
    n = ""
    while i > 8:
        y = str(i % 8)
        n = y + n
        i = int(i / 8)
    while i <= 8:
        i = str(i)
        n = i + n
        return n

def hex(i):
    #hexadecimal
    n = ""
    while i > 16:
        y = str(i % 16)
        if y == '10':
            y = 'A'
        elif y == '11':
            y = 'B'
        elif y == '12':
            y = 'C'
        elif y == '13':
            y = 'D'
        elif y == '14':
            y = 'E'
        elif y == '15':
            y = 'F'
        n = y + n
        i = int(i / 16)
    while i < 16:
        y = str(i)
        if y == '10':
            y = 'A'
        elif y == '11':
            y = 'B'
        elif y == '12':
            y = 'C'
        elif y == '13':
            y = 'D'
        elif y == '14':
            y = 'E'
        elif y == '15':
            y = 'F'
        n = y + n
        return n

for i in range(1,a+1):
    k = bi(i)
    m = int(octal(i))
    p = (hex(i))
    #decimal
    print('{0:3}'.format(i),'{0:3}'.format(m),p.rjust(3),k.rjust(4))

