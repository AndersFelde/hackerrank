import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(s):
    h = {}
    for x in range(len(s)):
        if s[x] in h:
            h[s[x]].append(x)
        else:
            h[s[x]] = [x]

    for k, v in h:
        if len(v) > 2:


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
