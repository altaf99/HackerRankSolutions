import numpy

inp = input()
inp=[int(n) for n in inp.split()]
#print(inp)

arry =numpy.array(inp)
print(numpy.reshape(arry,(3,3)))

