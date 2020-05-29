from collections import deque

d = deque()


for _ in range(int(input())):
    cmnd = "d."
    a = input().split()
    if len(a) > 1:
        cmnd += str(a[0]) + "(" + str(a[1]) + ")"
    else:
        cmnd += str(a[0]) + "()"

    eval(cmnd)

for x in d:
    print(x, end = " ")
