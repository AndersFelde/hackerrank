import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    m = {}
    count = 0

    for word in magazine:
        if word not in m:
            m[word] = 1
        else:
            m[word] += 1

    for word in note:
        if word in m and m[word] > 0:
            m[word] -= 1
            count += 1

    print("Yes") if count == len(note) else print("No")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
