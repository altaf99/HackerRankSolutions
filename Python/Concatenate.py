import numpy

inp = input()
inp=[int(x) for x in inp.split(" ")]
N=inp[0]    #1st matrix row
M=inp[1]    #2nd matrix row
P=inp[2]    #col

mat1=[]
mat2=[]
for i in range(N):
    row = list(map(int,input().split(" ")))
    
    mat1.append(row)

for i in range(M):
    row = list(map(int,input().split(" ")))
    
    mat2.append(row)

arry1 = numpy.array(mat1)
arry2 = numpy.array(mat2)
arry1=numpy.reshape(arry1,(N,P))
arry2=numpy.reshape(arry2,(M,P))
print(numpy.concatenate((arry1,arry2),axis=0))


