import numpy

inp = input()
inp=[int(x) for x in inp.split(" ")]
N=inp[0]
M=inp[1]

els=[]
for i in range(N):
    row = input().split(" ")
    for el in row:
        els.append(int(el))
#print(els)

arry = numpy.array(els)
arry=numpy.reshape(arry,(N,M))
print(numpy.transpose(arry))
print(arry.flatten())

