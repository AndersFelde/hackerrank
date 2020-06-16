import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    bribe = 0
    x = 0
    while x < len(q):
        if(q[x] < q[x-1] and x != 0):
            print("Too chaotic")
            return
        elif x == len(q)-1:
            print(bribe)
            return
        y = x+1
        b = False
        while q[x] > q[y]:
            if q[y] > q[y+1]:
                print("Too chaotic")
                return
            b = True
            y += 1
            bribe += 1
            if(y == len(q)):
                break

        if b:
            old = q[x]
            q.remove(q[x])
            q.insert(y-1, old)
            x -= 1
        x += 1
    print(bribe)
    return
    """ if(q[x+1] < q[x-1]) and x != 0:
            print("Too chaotic")
            return
        if(q[x+1] < q[x]):
            old = q[x]
            q[x] = q[x+1]
            q[x+1] = old
            bribe += 1
    print(bribe) """


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
