import numpy

a = list()
for _ in range(int(input())):
    a.append(list(map(float, input().split())))

print(round(numpy.linalg.det(a), 2))
