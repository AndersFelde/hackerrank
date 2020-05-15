if __name__ == '__main__':
    l = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())

        l.append([name, score])

    def sortSecond(val):
        return val[1]  # altså sort by score

    def sortFirst(val):
        return val[0]  # altså sort by score

    l.sort(key=sortSecond)

    first = l[0][1]

    for p in range(1, len(l)):
        if(l[p][1] != first):
            second = l[p][1]
            break

    result = list()
    for x in range(p, len(l)):
        i = l[x][1]
        if(i == second):
            result.append([l[x][0], l[x][1]])
            if(x == len(l)-1):
                result.sort(key=sortFirst)
                for student in result:
                    print(student[0])
                exit()

        else:
            result.sort(key=sortFirst)
            for student in result:
                print(student[0])
            exit()
