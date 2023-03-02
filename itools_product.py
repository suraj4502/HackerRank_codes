from itertools import product

a = map(int,input().split())
b = map(int,input().split())

axb = sorted(product(a,b))

for i in axb:
    print(i,end=" ")
    
    
    
    
"""
INPUT :
 1 2
 3 4
 
 OUTPUT :
 (1, 3) (1, 4) (2, 3) (2, 4)
 


"""
