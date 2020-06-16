import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    aCount = 0

    if(n < len(s)):
        for x in range(n):
            if s[x] == "a":
                aCount += 1

        return aCount

    diff = n % len(s)

    mult = (n - diff) / len(s)

    for x in s:
        if (x == "a"):
            aCount += 1 * mult

    for x in range(diff):
        if s[x] == "a":
            aCount += 1

    return int(aCount)


if __name__ == '__main__':
    """ fptr = open(os.environ['OUTPUT_PATH'], 'w')
 """
    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)

    """ fptr.write(str(result) + '\n')

    fptr.close() """

    """ x = 0
    y = 0
    while x < n:
        if s[y] == "a":
            aCount += 1
        y += 1
        if(y == len(s)-1):
            y = 0
        x += 1

    return aCount """
