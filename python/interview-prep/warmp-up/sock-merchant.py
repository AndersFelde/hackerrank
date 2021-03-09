import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    socks = {}
    for sock in ar:
        if str(sock) in socks:
            socks[str(sock)] += 1
        else:
            socks[str(sock)] = 1

    pairSum = 0
    for sock in socks:
        x = int(socks[str(sock)])
        if x % 2 > 0:
            x -= 1
        pairSum += x / 2
    return int(pairSum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
