if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    if(n < 2 or n > 10):
        exit()

    prev = arr[0]

    for i in arr:
        if i < -100 or i > 100:
            exit()
        if(prev != i):
            print(i)
            exit()
