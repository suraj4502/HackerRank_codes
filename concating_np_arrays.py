import numpy as np

mat1=[]
mat2=[]

n,m,p = map(int,input().split())
for i in range(n+m):
    inp = list(map(int,input().split()))
    if i < n:
        mat1.append(inp)
    else:
        mat2.append(inp)
        
print(np.concatenate((mat1,mat2),axis=0))





# -----------
import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print(numpy.concatenate((array_1, array_2), axis = 1))

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]    
