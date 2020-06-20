import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(a):
    change = 0
    while True:
        isChanged = False
        for x in range(len(a)):
            if(not a[x] == x+1):
                y = a[a[x]-1]
                a[a[x]-1] = a[x]
                a[x] = y
                isChanged = True
                change += 1
        if(not isChanged):
            return change


if __name__ == '__main__':
    """ fptr = open(os.environ['OUTPUT_PATH'], 'w') """

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    """ fptr.write(str(res) + '\n')

    fptr.close() """
