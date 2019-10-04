#!/usr/bin/env python

def fact(n):
    m = 1
    for i in range(1, n+1):
        m *= i
    return m

if __name__ == '__main__':
    number = int(input('Input a small number: '))
    print(fact(number))
