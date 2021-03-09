import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    bribe = 0
    h = {val: 0 for val in q}
    while True:
        isChanged = False
        for x in range(len(q)-1):
            if q[x] > q[x+1]:
                if(h[q[x]] == 2):
                    print("Too chaotic")
                    return
                y = q[x]
                q[x] = q[x+1]
                q[x+1] = y
                h[y] += 1
                isChanged = True
                bribe += 1

        if(not isChanged):
            print(bribe)
            return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
