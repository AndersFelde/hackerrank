for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    prev = 99999999999999999999999999999999999999999
    x = 0
    y = 1
    while len(lst) > 0:
        if lst[x] > prev and lst[len(lst)-y] > prev:
            print("No")
            break
        elif(len(lst[x:len(lst)-y]) == 1 and lst[x+1] <= prev):
            print("Yes")
            break
        elif lst[x] > lst[len(lst)-y] and lst[x] <= prev:
            prev = lst[x]
            x = x+1
        elif lst[x] < lst[len(lst)-y] and lst[len(lst)-y] <= prev:
            prev = lst[len(lst)-y]
            y = y+1
        elif lst[x] == lst[len(lst)-y]:
            x = x+1
            y = y+1
        else:
            print("No")
            break
