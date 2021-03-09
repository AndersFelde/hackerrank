import numpy

l = list()

l.append(input().split(" "))
l.append(input().split(" "))

l[0] = list(int(x) for x in l[0])
l[1] = list(int(x) for x in l[1])

A = numpy.array(l[0])
B = numpy.array(l[1])

print(numpy.inner(A, B))
print(numpy.outer(A, B))
