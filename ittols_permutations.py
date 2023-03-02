# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,k = input().split()

p = permutations(s,int(k))

l =[]
for i in p:
   l.append("".join(i))
   
fl=sorted(l)

for each in fl:
    print(each)
    
    
    
    
"""
HACK 2


out: 
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

"""
