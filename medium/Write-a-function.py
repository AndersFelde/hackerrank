def is_leap(y):
    if year < 1900 or year > 100000:
        print("Number must be between 1900 and 10^5")
        exit()
    leap = False

    if not year % 4:
        leap = True
        if year % 100:
            leap = False
            if not year % 400:
                leap = True

    return leap


year = int(input())
print(is_leap(year))
