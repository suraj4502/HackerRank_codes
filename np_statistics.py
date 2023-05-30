import numpy as np
'''
mean along axis 1
variance along axis 0
std 
'''
n,m = map(int,input().split())

arr = np.array([input().split() for _ in range(n)],int)

mean = np.mean(arr,1)
var = np.var(arr,0)
std = np.std(arr,None)

print(mean, var, round(std,11),  sep='\n')
