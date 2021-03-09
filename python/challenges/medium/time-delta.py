import math
import os
import random
import re
import sys

import calendar
from calendar import monthrange
from datetime import datetime
abbr_to_num = {name: num for num,
               name in enumerate(calendar.month_abbr) if num}


def time_delta(t1, t2):
    arr1 = t1.split()
    arr2 = t2.split()

    if arr1[4] == arr2[4] or arr1[5] == arr1[5]:
        time1 = arr1[5].split(":")
        date1 = arr1[1]
        month1 = abbr_to_num[arr1[2]]
        year1 = arr1[3]

        time2 = arr2[5].split(":")
        date2 = arr2[1]
        month2 = abbr_to_num[arr2[2]]
        year2 = arr2[3]
    else:
        arr1 = convert(arr1)
        arr2 = convert(arr2)

        time1 = arr1[0].split(":")
        date1 = arr1[1]
        month1 = arr1[2]
        year1 = arr1[3]

        time2 = arr2[0].split(":")
        date2 = arr2[1]
        month2 = arr2[2]
        year2 = arr2[3]

    a = datetime.datetime(year1, month1, date1, time1[0], time1[1], time1[2])
    b = datetime.datetime(year2, month2, date2, time2[0], time2[1], time2[2])

    return((a-b).total_seconds())

    """ day1 = arr1[0]
    date1 = arr1[1]
    month1 = arr1[2]
    year1 = arr1[3]
    time1 = arr1[4]
    tzone1 = arr1[5]

    day2 = arr2[0]
    date2 = arr2[1]
    month2 = arr2[2]
    year2 = arr2[3]
    time2 = arr2[4]
    tzone2 = arr2[5] """


def convert(arr):

    tDiff = arr[5]
    mins = arr[4].split(":")[10] * 60 + arr[4].split(":")[1]
    date, year = arr[1], arr[3]
    month = abbr_to_num[arr[2]]

    diffMins = tDiff[3] + tDiff[1:2]*60

    mins = mins + diffMins

    hours = str(mins // 60)
    mins = str(mins % 60)

    if hours > 23:
        hours = hours - 24
        date += 1
        if(date > monthrange(year, month)[1]):
            date = date - monthrange(year, month)[1]
            month += 1
            if(month > 12):
                year += 1
                month = 1

    newTime = "{}:{}:{}".format(hours, mins, arr[4][6:8])
    return [newTime, date, month, year]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
