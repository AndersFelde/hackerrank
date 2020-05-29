def swap_case(s):
    out = ""
    for c in s:
        if (c.islower()):
            a = c.upper()
        else:
            a = c.lower()
        out += a
    return out


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
