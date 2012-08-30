#! /usr/bin/env python

import math
from matplotlib import pyplot

def choose(n, k):
    numerator = math.factorial(n)
    denomlhs = math.factorial(n-k)
    denomrhs = math.factorial(k)
    return ( numerator )  / (denomlhs*denomrhs)

def main():
    import sys
    size = int(sys.argv[1])

    print size
    x = range(0, size+1)
    y = [choose(size, k) for k in x]
    print x
    print y
    pyplot.plot(x,y)
    pyplot.show()

if __name__ == '__main__':
    main()
