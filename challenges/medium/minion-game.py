def minion_game(string):
    s = string
    vowels = "AEIOU"

    kPoint = 0  # vowels
    sPoint = 0  # consonants

    for x in range(len(s)):
        if s[x] in vowels:
            kPoint += len(s)-x
        else:
            sPoint += len(s)-x

    if kPoint > sPoint:
        print("Kevin " + str(kPoint))
    elif kPoint < sPoint:
        print("Stuart " + str(sPoint))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
