import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, q):
    high = 0
    l = list()
    for _ in range(n):
        l.append(0)

    for x in range(len(q)):
        t = q[x]
        for y in range(t[0]-1, t[1]):
            l[y] += t[2]
            if l[y] > high:
                high = l[y]

    return high


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
