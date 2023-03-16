s,n = input().split()



from itertools import combinations



combs = []
for i in range(1, int(n)+1):
    combs += combinations(sorted(s), i)

for i in combs:
    print("".join(i))


    
"""
write a python script that takes 'HACK 2' as input and gives the following output 'A
C
H
K
AC
AH
AK
CH
CK
HK'

"""
