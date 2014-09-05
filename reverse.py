#!/usr/bin/python
import math


nr = 12345678


def r(nr, order):
    if nr == math.ceil(nr / 10):
        return (10 ** order ) * nr
    digit = nr % 10
    return int((10 ** order) * digit + r(math.floor(nr / 10), order - 1))


def main():
    x = nr
    l = 0
    while x > 0:
        x = x / 10
        l += 1
    print r(nr, l - 1)


if __name__ == "__main__":
    main()

