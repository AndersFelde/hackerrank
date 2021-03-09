import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(a):
    pSum = -9999999**9

    for x in range(len(a)-2):
        for y in range(len(a[0])-2):
            nSum = a[x][y]
            nSum += a[x][y+1]
            nSum += a[x][y+2]
            nSum += a[x+1][y+1]
            nSum += a[x+2][y]
            nSum += a[x+2][y+1]
            nSum += a[x+2][y+2]
            if nSum > pSum:
                pSum = nSum

    return pSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
