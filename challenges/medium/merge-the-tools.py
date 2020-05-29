def merge_the_tools(string, k):
    s = string
    n = len(s)

    if n % k > 0 or n < 1 or n > 10000 or k < 1 or k > n:
        exit()
    split = int(n/k)
    i = 0
    outList = list()
    for x in range(split):
        outList.append(s[i:i + int(n/split)])
        i = i + split

    result = list()

    def checker(x, o):
        if x >= len(o):
            result.append(o)
            if(len(result) == split):
                for a in result:
                    print(a)

    for out in outList:
        print(out)
        x = 0
        while x < len(out):  # for hver bokstav i out
            check = out[x]
            z = x + 1
            x = x + 1
            checker(x, out)
            while z < len(out):  # for hver bokstav i posisjon x + 1
                if(check == out[z]):
                    out = out[:z] + out[z + 1:]
                checker(x, out)
                z = z+1


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
