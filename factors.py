#!/usr/bin/python3

import sys
from primes import factors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(1)
    num = []
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
    for i in lines:
        num.append(int(i))
    for i in num:
        j = factors(i)
        if j != 1:
            if i % 2 == 0:
                j = 2
            else:
                for j in range(3, (i//2) + 1, 2):
                    if (i % j == 0):
                        j = i // j
                        break
            print("{} = {:d}*{}".format(i, i//j, j))
