import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    count = {}
    for x in arr:
        for y in x:
            if y in count:
                count[y] += 1
            else:
                count[y] = 1

    sortedCount = sorted(count.items(), reverse=True)
    length = 0
    a = 0
    for key, value in sortedCount:
        if length + int(value) > 7:
            mult = int(length - 7)
            a += int(int(key) * mult)
            break

        a += int(int(key) * int(value))
        length += value

    return a


if __name__ == '__main__':
    """ fptr = open(os.environ['OUTPUT_PATH'], 'w') """

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)
    """ fptr.write(str(result) + '\n')

    fptr.close()
 """
