import math


def sine(x):
    return x - pow(x, 3) / factorial(3) + pow(x, 5) / factorial(5) - pow(x, 7) / factorial(7)


def cosine(x):
    return 1 - pow(x, 2) / 2 + pow(x, 4) / math.factorial(4) - pow(x, 6) / math.factorial(6)


def remainder(x, y):
    return x - int(x / y) * y


def factorial(x):
    output = 1
    while x != 1:
        output *= x
        x -= 1
    return output


def power(base, exp):
    output = 1
    while exp > 0:
        latest_bit = (exp & 1)
        if latest_bit:
            output *= base
        base = base * base
        exp = exp >> 1
    return output


def tangent(x):
    return x + power(x, 3)/3 + 2/power(15, 5)*power(x, 5)


def cotangent(x):
    return 1/x - x/3 - power(x, 3)/45
