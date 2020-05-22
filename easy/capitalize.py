#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):
    words = s.split()
    out = list()
    for c in words:
        if(c[0].isalpha()):
            out.append(c.capitalize())
        else:
            out.append(c)
        if(len("".join(out)) == len(s)):
            return "".join(out)
        while s[len("".join(out))] == " ":
            out.append(" ")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
