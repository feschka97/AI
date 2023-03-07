PI = 3.141592653589793


def sine(x):
    match x:
        case "x <= 1 && x >= -1":
            return x - power(x, 3) / 6 + pow(x, 5) / 120 - power(x, 7) / 5040
        case "x <=2 && x >=-2":
            return x - power(x, 3) / 6 + pow(x, 5) / 120 - power(x, 7) / 5040 + power(x, 9) / 362880
        case "x <=3 && x >=-3":
            return x - power(x, 3) / 6 + pow(x, 5) / 120 - power(x, 7) / 5040 + power(x, 9) / 362880 - power(x,11) / factorial(11)
        case "x <=6 && x >=-6":
            return x - power(x, 3) / 6 + pow(x, 5) / 120 - power(x, 7) / 5040 + power(x, 9) / 362880 - power(x,11) / factorial(11) + power(x, 13) / factorial(13)


def cosine(x):
    match x:
        case "x <= 1 && x >= 1":
            return 1 - power(x, 2) / 2 + power(x, 4) / factorial(4) - power(x, 6) / factorial(6)
        case "":
            1 - power(x, 2) / 2 + power(x, 4) / factorial(4) - power(x, 6) / factorial(6) + power(x, 8) / factorial(8)


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
    if mod(x) < PI / 2:
        return x + power(x, 3) / 3 + 2 / power(15, 5) * power(x, 5)
    else:
        return "NaN"


def cotangent(x):
    return 1 / x - x / 3 - power(x, 3) / 45


def mod(x):
    if x < 0:
        return -x
    else:
        return x
