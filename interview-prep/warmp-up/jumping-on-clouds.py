import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    x = 0
    jumps = 0
    while True:
        if(x == len(c)-1):
            break
        elif x + 1 == len(c)-1:
            jumps += 1
            break

        if(c[x+2]) == 0:
            x += 2
        else:
            x += 1
        jumps += 1

    return jumps


if __name__ == '__main__':
    """     fptr = open(os.environ['OUTPUT_PATH'], 'w')"""
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)

    """ fptr.write(str(result) + '\n')

        fptr.close() """
