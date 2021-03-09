import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(n, s):
    pos = 0
    valley = 0

    for x in s:
        if (x == "D"):
            pos -= 1
        else:
            pos += 1

        if pos == 0 and x == "U":
            valley += 1

    return valley


if __name__ == '__main__':
    """ fptr = open(os.environ['OUTPUT_PATH'], 'w') """

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)

    """ fptr.write(str(result) + '\n')

    fptr.close() """
