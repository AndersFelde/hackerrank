from iterools import product

A = input().split()
B = input().split()

out = list()

for x in list(product(A, B)):
    temp = list()
    for y in x:
        temp.append(int(y))
    out.append(temp)
