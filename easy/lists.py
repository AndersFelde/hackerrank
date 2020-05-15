if __name__ == '__main__':
    N = int(input())
    lst = list()
    for _ in range(N):
        cmnds = list(input().split())

        if(len(cmnds) == 2):
            eval("lst." + cmnds[0] + "(" + cmnds[1] + ")")
        elif len(cmnds) == 3:
            eval("lst." + cmnds[0] + "(" + cmnds[1] + ", " + cmnds[2] + ")")
        else:
            if(cmnds[0] == "print"):
                print(lst)
            else:
                eval("lst." + cmnds[0] + "()")
