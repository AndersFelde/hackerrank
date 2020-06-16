#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.


def rotLeft(a, d):
    nList = list()
    if d <= (len(a)-1):
        nList.append(a[d:])
        nList.append(a[:d])
    else:
        while d > len(a)-1:
            d = d - len(a) - 1
        a.reverse()
        nList.append(a[d:])
        nList.append(a[:d])

    return list(map(str, nList[0])) + list(map(str, nList[1]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
